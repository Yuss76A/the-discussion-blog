from django.shortcuts import render
from django.http import HttpResponse

def welcome(request):
    return HttpResponse("<h1>Discussion Blog</h1>")

def about(request):
    return HttpResponse("<h1>What This Blog Is About</h1>")
