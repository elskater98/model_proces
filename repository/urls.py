from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns=[
    path('', views.homepage, name='homepage'),
    path('urban/', views.urban_page, name='urban'),
]