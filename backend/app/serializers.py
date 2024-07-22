from rest_framework import serializers

class XMLFileSerializer(serializers.Serializer):
    xml_file = serializers.FileField()
