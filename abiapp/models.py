import datetime
from telnetlib import STATUS
from django.db import models
from embed_video.fields import EmbedVideoField
# from django.utils.text import slugify
# from django.db.models.signals import pre_save

#Create your models here.
class Banner(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/images')
    date = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.title 



class Category(models.Model):
      name = models.CharField(max_length=200)
      image = models.ImageField(upload_to='media/category/images')
      date = models.DateField(auto_now_add=True)
      title = models.CharField(max_length=200)
      containt = models.TextField()
      slug = models.SlugField()
      
      def __str__(self):
        return   self.title
        


class Video(models.Model):
    category  =  models.ForeignKey(Category,on_delete=models.CASCADE)
    thumbnail = models.ImageField(upload_to='media/thumbnail/images')
    video_url = EmbedVideoField()
    title = models.CharField(max_length=200)
    containt = models.TextField()
    price = models.IntegerField()
    slug = models.SlugField()
      
    def __str__(self):
        return   self.title


