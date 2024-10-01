from django.shortcuts import render

from apidjango.mongodb import MongoConnection
from rest_framework import viewsets, status
from rest_framework.response import Response
import pandas as pd
from .serializers import ExcelSerializer

db, client = MongoConnection.get_db_handle("pandas_db")
document_collection = MongoConnection.get_collection_handle(db, "pandas")

class PandasViewSet(viewsets.ViewSet):

    serializer_class = ExcelSerializer

    def create(self, request):

        excel_serializer = self.serializer_class(data=request.data)

        if excel_serializer.is_valid():
            valid_excel = excel_serializer.validated_data
            df = pd.read_excel(valid_excel["document"], engine='openpyxl')
            return Response("<h1>Hello World!</h1>", status=status.HTTP_200_OK)
        else:
            return Response({"error": "Serializer is not valid"}, status=status.HTTP_400_BAD_REQUEST)
