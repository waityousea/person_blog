from django.db import models

# Create your models here.


class Gallery(models.Model):
    description = models.CharField(default='在这里写作品的简介', max_length=100)
    image = models.ImageField(upload_to='images/', default='default.png')
    title = models.CharField(default='作品标题', max_length=50)
    # music = models.ImageField(upload_to='musics/', default='default.mp3')
    # video = models.ImageField(upload_to='videos/', default='default.mp4')

    def __str__(self):
        return self.title


