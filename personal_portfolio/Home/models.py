from django.db import models

class home_page(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)

class about_me(models.Model):
    first_title = models.CharField(max_length=100)
    first_caption = models.CharField(max_length=10000)
    second_caption = models.CharField(max_length=10000)
    second_title = models.CharField(max_length=100)
    li_1 = models.CharField(max_length=100,default="")
    li_2 = models.CharField(max_length=100,default="")
    li_3 = models.CharField(max_length=100,default="")
    li_4 = models.CharField(max_length=100,default="")
    li_5 = models.CharField(max_length=100,default="")


    