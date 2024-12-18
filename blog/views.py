from django.shortcuts import render
from django.http import HttpResponse

def welcome(request):
    return render(request, 'blog/welcome.html')

def about(request):
    return render(request, 'blog/about.html')
