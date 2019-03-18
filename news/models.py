from django.db import models
import datetime as dt
  
class Category (models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()

class Location (models.Model): 
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name 

    def save_location(self):
        self.save()

class Image(models.Model): 
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=1024)
    image = models.ImageField(upload_to = 'image/')
    location = models.ForeignKey(Location)
    category = models.ForeignKey(Category)
    capture_date= models.TimeField(auto_now_add=True)

    @classmethod
    def search_by_category(cls,search_term):
        category=Category.objects.filter(name__icontains=search_term)
        images = cls.objects.filter(category=category)
        return images

    def save_image(self):
        self.save()

    @classmethod
    def get_image_by_id(cls, id):
        try:
            image=Image.objects.get (id =id)
            return image
        except DoesNotExist:
            return image.objects.get(id=1)
        