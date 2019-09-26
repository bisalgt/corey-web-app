from django.shortcuts import render
from .models import Post



def home(request): # gets request from url as first argument// we can name any
    context = {
        'posts':Post.objects.all()
    }
    return render(request, 'blog/home.html',context)

def about(request):
    return render(request, 'blog/about.html',{'title':'About'})