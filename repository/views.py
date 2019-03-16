from django.shortcuts import render
from .models import *
# Create your views here.

def homepage(request):
    photo = Photo.objects.all().order_by('-date')
    theme= Theme.objects.all()
    author= Author.objects.all()
    return render(request,'homepage.html',context={'photo':photo,'theme':theme,'author':author})

def abstract(request):
    photo = Photo.objects.filter(select_theme__name__contains='abstract').order_by('-date')
    theme = Theme.objects.all()
    author = Author.objects.all()
    return render(request, 'abstract.html', context={'photo':photo, 'theme':theme, 'author':author})

def nature(request):
    photo = Photo.objects.filter(select_theme__name__contains='nature').order_by('-date')
    theme = Theme.objects.all()
    author = Author.objects.all()
    return render(request, 'nature.html', context={'photo':photo, 'theme':theme, 'author':author})

def minimal(request):
    photo = Photo.objects.filter(select_theme__name__contains='minimal').order_by('-date')
    theme = Theme.objects.all()
    author = Author.objects.all()
    return render(request, 'minimal.html', context={'photo':photo, 'theme':theme, 'author':author})

