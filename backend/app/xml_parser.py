import xml.etree.ElementTree as ET
from .models import RHBA  

def parse_xml_content(xml_content):
    root = ET.fromstring(xml_content)

    ns = {'oval': 'http://oval.mitre.org/XMLSchema/oval-definitions-5'}

    for definition in root.findall('.//oval:definition', ns):
        cves = []
        cvss_values = []
        cwe_values = []

        # Список для хранения описаний CVE с CVSS и CWE
        description_cve_list = []

        for cve in definition.findall('.//oval:cve', ns):
            cve_text = cve.text
            cvss = cve.attrib.get('cvss3', '')
            cwe = cve.attrib.get('cwe', '')

            
            description_cve_list.append(f"{cve_text} (CVSS: {cvss}, CWE: {cwe})")
            cves.append(cve_text)
            cvss_values.append(cvss)
            cwe_values.append(cwe)

        patches = definition.find('.//oval:title', ns).text
        rhba = definition.find('.//oval:reference[@source="RHSA"]', ns).attrib.get('ref_id', '')
        cpe_list = [cpe.text for cpe in definition.findall('.//oval:cpe', ns)]
        description = definition.find('.//oval:description', ns).text

        
        unique_packages = set()
        for bugzilla in definition.findall('.//oval:bugzilla', ns):
            full_text = bugzilla.text
            if full_text and ":" in full_text:
                package_name = full_text.split(":")[0]
                unique_packages.add(package_name)

        # Создание экземпляра модели RHBA
        rhba_instance = RHBA(
            CVEs=', '.join(cves),
            Patches=patches,
            RHBA=rhba,
            CPE_list=', '.join(cpe_list),
            description=description,
            description_cve='; '.join(description_cve_list),  
            criteria=', '.join([criterion.attrib.get('comment', '') for criterion in definition.findall('.//oval:criterion', ns)]),
            packages=', '.join(unique_packages)
        )

        # Сохранение экземпляра в базе данных
        rhba_instance.save()

        print(f'Saved RHBA instance with RHBA ID: {rhba_instance.id}')

