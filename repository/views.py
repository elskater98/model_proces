from django.shortcuts import render
from .models import Photo,History_connections

# Create your views here.

def index(request):
    return render(request,'index.html')