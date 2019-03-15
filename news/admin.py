from django.contrib import admin
from .models import Category,Location,Image
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    filter_horizontal =('category',)

admin.site.register(Category)
admin.site.register(Location)
admin.site.register(Image)