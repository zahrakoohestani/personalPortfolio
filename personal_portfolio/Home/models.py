from django.db import models

class Data(models.Model):
    text = models.CharField(max_length=100)
    image = models.ImageField(upload_to='home/images', default="")
    long_text = models.TextField(default="")