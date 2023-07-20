from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def first_string(request):
    return HttpResponse("<h1><marquee>This is my first String</h1></marquee>")

def second_string(request):
    return HttpResponse('<h2><marquee>This is my second String</h1></marquee>')