from django.db import models

# Create your models here.


class Blog(models.Model):
    title = models.CharField(default='博文标题', max_length=50)
    data = models.DateField()
    image = models.ImageField(upload_to='images/', default='default.png')
    text = models.TextField(default='正文')

    def __str__(self):
        return self.title

    def short_text(self):
        return self.text[:70]+"......"