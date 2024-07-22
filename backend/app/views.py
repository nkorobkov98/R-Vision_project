from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import XMLFileSerializer
from .xml_parser import parse_xml_content


class XMLFileUploadView(APIView):
       def post(self, request):
           uploaded_file = request.FILES['xml_file']
           xml_content = uploaded_file.read().decode('utf-8')

           parse_xml_content(xml_content)

           return Response({'message': 'XML файл успешно обработан.'})