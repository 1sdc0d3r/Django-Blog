from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Braden',
        'title': 'Blog Post 1',
        'content': 'First Post content',
        'date_posted': 'May 14, 2020'
    },
    {
        'author': 'John Doe',
        'title': 'Blog Post 2',
        'content': 'Second Post content',
        'date_posted': 'May 15, 2020'
    },
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
