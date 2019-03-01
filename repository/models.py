from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Photo(models.Model):
    name = models.CharField(max_length=200,help_text="Enter a name to the snap",null=False)
    picture=models.ImageField(upload_to='repository/images/',help_text='Choose a picture')

    RESOLUTION_STATUS = (('HD',('1280×720 píxels')), ('FHD','1920×1080 pixels'),
                         ('QHD','2560*1440 pixels'), ('UHD','3840×2160 píxels'))

    select_resolution=models.CharField(max_length=3, choices=RESOLUTION_STATUS, blank=False, default='FHD',
                              help_text='Pick up the resolution')

    RATING_CHOICES=((1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five'))

    rating = models.PositiveSmallIntegerField('Rating (stars)', blank=False, default=3, choices=RATING_CHOICES)

    author=models.ForeignKey(User,default=1,on_delete=models.SET_DEFAULT)

    def __str__(self):
        return str(self.picture)

class History_connections(models.Model):
    date = models.DateTimeField()

