from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse("Welcome to my home page")

def products(request):
    return HttpResponse("Welcome to my products page")

def about(request):
    return HttpResponse("This is my about page")

def contact(request):
    return HttpResponse("If you wish to contact me")

def services(request):
    return HttpResponse("My services are on the home page ")


