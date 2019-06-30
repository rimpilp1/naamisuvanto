from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def homepage(request):
    return HttpResponse("Homepage")

def test(request):
    template_name = 'common/generic.html'
    context = {

    }
    return render(request,template_name,context)

def link1(request):
    template_name = 'common/link1.html'
    context = {

    }
    return render(request,template_name,context)

def link2(request):
    template_name = 'common/link2.html'
    context = {

    }
    return render(request,template_name,context)