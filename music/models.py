from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Albums(models.Model):

    artist = models.CharField(max_length = 250)
    ablum_title = models.CharField(max_length = 500)
    genre = models.CharField(max_length = 100)
    album_logo = models.CharField(max_length = 1000)

    def __str__(self):
        return self.artist + ' - ' + self.ablum_title

class Songs(models.Model):

    album = models.ForeignKey(Albums,on_delete = models.CASCADE)
    file_type = models.CharField(max_length = 50)
    song_title = models.CharField(max_length = 100)
    is_favourite = models.BooleanField(default = False)

    def __str__(self):
        return self.song_title