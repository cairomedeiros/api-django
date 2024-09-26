from django.shortcuts import render

from apidjango.mongodb import MongoConnection
from rest_framework import viewsets, status
from rest_framework.response import Response

class PandasViewSet(viewsets.ViewSet):
    def create(self, request):
        db, client = MongoConnection.get_db_handle("teste")
        return Response("<h1>Hello World!</h1>", status=status.HTTP_200_OK)
