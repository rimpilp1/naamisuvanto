from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .forms import SaalisForm
from .models import Saalis
import datetime
from django.utils import timezone


def index(request):
    now = timezone.now()
    saaliit = Saalis.objects.filter(saantipaiva__year=now.year).order_by('saantipaiva')[:5]
    template_name = 'saalistilastot.html'
    context = {
        'saaliit': saaliit,
    }
    return render(request,template_name,context)

def post(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        form = SaalisForm(request.POST, request.FILES or None)
        if form.is_valid():
            instance = form.save(commit = False) 
            instance.save()
            return HttpResponse("Thanks")

        else:
            return HttpResponse("Invalid form")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SaalisForm()
    return render(request, 'form.html', {'form': form})

def biggest(request):
    saaliit = Saalis.objects.order_by('-paino')[:1].first()
    template = loader.get_template('suurin.html')
    context = {
        'suurin': saaliit,
    }
    return HttpResponse(template.render(context, request), mimetype="application/x-javascript")


def table(request):
    saaliit = Saalis.objects.order_by('saantipaiva')[:5]
    template = loader.get_template('result.html')
    context = {
        'saaliit': saaliit,
    }
    return HttpResponse(template.render(context, request))

# Create your views here.
