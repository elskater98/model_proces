from django.shortcuts import render
from .models import *
# Create your views here.


def homepage(request):
    photo = Photo.objects.all()
    theme= Theme.objects.all()
    author= Author.objects.all()
    return render(request,'homepage.html',context={'photo':photo,'theme':theme,'author':author})

def abstract(request):
    photo = Photo.objects.filter(select_theme__name__contains='abstract')
    theme = Theme.objects.all()
    author = Author.objects.all()
    return render(request, 'abstract.html', context={'photo':photo, 'theme':theme, 'author':author})