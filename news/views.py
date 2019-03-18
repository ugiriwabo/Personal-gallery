from django.shortcuts import render,redirect
from django.http  import HttpResponse
from .models import Image
import datetime as dt

# Create your views here.
def welcome(request):
    return render(request, 'all-news/welcome.html')

def image(request):
    images = Image.objects.all()
    
    return render(request,'all-news/welcome.html',{'images':images })

def search_results(request):

    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_images = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})



        

    
    