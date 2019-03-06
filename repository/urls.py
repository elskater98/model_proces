from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$', views.homepage, name='homepage'),
    url(r'^$', views.urban_page, name='urban'),
]