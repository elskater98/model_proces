from django.shortcuts import render
from .models import Photo
# Create your views here.


def homepage(request):
    photo = Photo()
    return render(request,'homepage.html',context={'photo':photo})