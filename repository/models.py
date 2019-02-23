from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Photo(models.Model):
    name = models.CharField(max_length=20, null=False)
    picture = models.ImageField(upload_to='repository/images')

    RESOLUTION_STATUS = (('HD', '1280×720 píxels'), ('FHD', '1920×1080 pixels'),
                         ('QHD', '2560*1440 pixels'), ('UHD', '3840×2160 pixels'))

    select_resolution = models.CharField(max_length=3, choices=RESOLUTION_STATUS, blank=False, default='FHD')

    RATING_CHOICES = ((1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five'))

    rating = models.PositiveSmallIntegerField('Rating (stars)', blank=False, default=3, choices=RATING_CHOICES)

    author = models.ForeignKey(User, default=1, on_delete=models.SET_DEFAULT)

    def __str__(self):
        return "{0} {1}".format(self.name, self.author)


class HistoryConnection(models.Model):
    authorOfConnection = models.ForeignKey(User, default=1, on_delete=models.SET_DEFAULT)
    date = models.DateTimeField()

    def __str__(self):
        string = "{0} => {1}"
        return string.format(self.authorOfConnection, self.date)


class ProfileUser(models.Model):
    userName = models.CharField(max_length=20)
    userNickName = models.CharField(max_length=20)
    favouriteImage = models.ForeignKey(Photo, default=1, on_delete=models.SET_DEFAULT)

    def __str__(self):
        string = "{0} alias {1} has {2} as favourite image"
        return string.format(self.userName, self.userNickName, self.favouriteImage)
