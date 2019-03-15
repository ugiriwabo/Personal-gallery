from django.db import models

# Create your models here.

class Image(models.Model):
    title = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=1024)
    image_location = db.Column(db.Integer,db.ForeignKey("image_location"))
    image_category = db.Column(db.Integer,db.ForeignKey("image_category"))

   
        