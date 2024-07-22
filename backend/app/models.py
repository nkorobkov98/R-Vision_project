from django.db import models

# Create your models here.

class RHBA(models.Model):
    id = models.AutoField(primary_key=True)
    CVEs = models.TextField(blank=True, null=True, default="")
    Patches = models.TextField(blank=True, null=True, default="")
    RHBA = models.TextField(blank=True, null=True, default="")
    CPE_list = models.TextField(blank=True, null=True, default="")
    description = models.TextField(blank=True, null=True, default="")
    description_cve = models.TextField(blank=True, null=True, default="")
    criteria = models.TextField(blank=True, null=True, default="")
    packages = models.TextField(blank=True, null=True, default="")

    class Meta:
        db_table = 'RHBA'
        ordering = ['pk']