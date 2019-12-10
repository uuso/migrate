from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from newapp.models import Dummy

# Create your views here.

def index(request):
    data = { "objects": Dummy.objects.all() }
    template = loader.get_template("index.html")
    return HttpResponse(template.render(data))