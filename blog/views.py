from django.shortcuts import render
# from django.http import HttpResponse 


posts = [
    {
        'author':'Bishal Gautam',
        'title':'Blog Post 1',
        'content':'First Post Content',
        'date_posted':'August 28, 2018'
    },
    {
        'author':'Jane Doe',
        'title':'Blog Post 2',
        'content':'Second Post Content',
        'date_posted':'August 29, 2018'
    },

]


def home(request): # gets request from url as first argument// we can name any
    context = {
        'posts':posts
    }
    return render(request, 'blog/home.html',context)

def about(request):
    return render(request, 'blog/about.html',{'title':'About'})