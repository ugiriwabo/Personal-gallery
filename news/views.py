from django.shortcuts import render,redirect
from django.http  import HttpResponse
from .models import Image
import datetime as dt

# Create your views here.
def welcome(request):
    return render(request, 'all-news/welcome.html')

def image(request):
    images = Image.objects.all()
    return render(request,'all-news/welcome.html',{'images':images})

def search_results(request):

    if 'article' in request.GET and request.GET["article"]:
        search_term = request.GET.get("article")
        searched_articles = Article.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'all-news/search.html',{"message":message,"articles": searched_articles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-news/search.html',{"message":message})



        

    
    