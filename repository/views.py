from django.shortcuts import render
from .models import *
# Create your views here.


def homepage(request):
    photo = Photo.objects.all()
    return render(request,'homepage.html',context={'photo':photo})

#def urban_page(request):
#    photo = Photo.objects.all()
#    return render(request, 'urban.html', context={'photo': photo})