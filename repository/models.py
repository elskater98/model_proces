from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Theme(models.Model):
    name = models.CharField(max_length=32, default="", blank=False)

    def __str__(self):
        return self.name

class Photo(models.Model):
    name = models.CharField(max_length=64, help_text="Enter a name to the snap", null=False)

    picture = models.ImageField(default="default.png", null=False)

    author = models.ForeignKey(User, default=1, on_delete=models.SET_DEFAULT)

    select_theme=models.ManyToManyField(Theme, blank=True)

    RESOLUTION_STATUS = (('HD', '1280×720 píxels'), ('FHD', '1920×1080 pixels'),
                         ('QHD', '2560*1440 pixels'), ('UHD', '3840×2160 pixels'))

    select_resolution = models.CharField(max_length=4, choices=RESOLUTION_STATUS, blank=False, default='FHD')

    RATING_CHOICES = ((1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five'))

    rating = models.PositiveSmallIntegerField('Rating (stars)', blank=False, default=3, choices=RATING_CHOICES)

    date = models.DateTimeField(auto_now_add = True,blank=True,null=True)

    def __str__(self):
        return self.name+"  "+self.author.get_short_name()








