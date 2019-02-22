from django.db import models

# Create your models here.

class Photo(models.Model):
    name = models.CharField(max_length=200,help_text="Enter a name ")
    resolution = models.CharField(help_text="Enter a name ")


