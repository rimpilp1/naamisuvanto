from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .forms import SaalisForm
from .models import Saalis


def index(request):
    return HttpResponse("Here you should be able to view fishing data")

def post(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        form = SaalisForm(request.POST, request.FILES or None)
        if form.is_valid():
            instance = form.save(commit = False) 
            instance.save()
        """
		# create a form instance and populate it with data from the request:
        form = SaalisForm(request.POST)
        # check whether it's valid:
        #if form.is_valid():
        kala = kalat()
        kala.paikka = request.POST.get('paikka')
        kala.saaja = request.POST.get('saaja')
        kala.viehe = request.POST.get('viehe')
        kala.paino = request.POST.get('paino')
        kala.pituus = request.POST.get('pituus')
        kala.save()
        # process the data in form.cleaned_data as required
        # ...
        # redirect to a new URL:
		"""
        return HttpResponse("Thanks")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SaalisForm()

    return render(request, 'form.html', {'form': form})

def table(request):
    saaliit = Saalis.objects.order_by('-id')[:5]
    template = loader.get_template('result.html')
    context = {
        'saaliit': saaliit,
    }
    return HttpResponse(template.render(context, request))

# Create your views here.
