from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date

# Create your models here.
class Imatge(models.Model):
    name = models.TextField()
    qualification = models.TextField()
    resolution = models.TextField()
    options = models.TextField()
    theme = models.TextField()
    author_name = models.ForeignKey(User,default=1,on_delete=models.SET_DEFAULT)


class History:
    date=models.DateField(default=date.today)
