from django.db import models

# Create your models here.
  
class Category (models.Model):
    name = models.CharField(max_length=30)

class Location (models.Model): 
    name = models.CharField(max_length=30) 

class Image(models.Model):
    title = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=1024)
    location = models.ForeignKey(Location)
    category = models.ForeignKey(Category)