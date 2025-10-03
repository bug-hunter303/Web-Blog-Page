from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'RamBS',
        'title': 'Blog Post 1',
        'content': 'First Post Content',
        'date_posted': 'Oct4 , 2025',
    },
    {
        'author': 'RBS',
        'title': 'Blog Post 2',
        'content': 'Second Post Content',
        'date_posted': 'Oct4 , 2024',
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html',{'title': 'About'})
