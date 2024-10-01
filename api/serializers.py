from rest_framework import serializers


class ExcelSerializer(serializers.Serializer):
    document = serializers.FileField(required=True)