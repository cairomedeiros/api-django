from django.shortcuts import render

from django.http import HttpResponse

from apidjango.mongodb import MongoConnection
# Create your views here.
def index(request):
    db, client = MongoConnection.get_db_handle("teste")
    return HttpResponse("<h1>Hello World!</h1>")
