from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Here you can view blog")


def post(request):
    return HttpResponse("Here you can post for blog")

# Create your views here.
