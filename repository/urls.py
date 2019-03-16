from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns=[
    path('', views.homepage, name='homepage'),
    path('abstract/', views.abstract, name='abstract'),
    path('nature/', views.nature, name='nature'),
    path('minimal/',views.minimal, name='minimal'),

]