from django.shortcuts import render
from django.shortcuts import redirect

from django.shortcuts import redirect
from .models import Sightings
from .forms import SightingsForm
import json

def index(request):
    return HttpResponse("It works!")

def map(request):
    content = Sightings.objects.all()
    context = {'sightings': content}
    return render(request,'census/map.html',context)

def stats(request):
    sightings = Sightings.objects.all() 
    context = {'content': sightings}
    return render(request, "census/stats.html", context)

def display(request):
    sightings = Sightings.objects.all()
    context = {'content': sightings}
    return render(request, "census/sightings.html", context)

def edit(request, squirrel_id):
    squirrel = Sightings.objects.get(Unique_Squirrel_ID=squirrel_id)
    if request.method == 'POST':
        form = SightingsForm(request.POST, instance=squirrel)
        if form.is_valid():
            form.save()
            return redirect(f'/census/sightings/{squirrel_id}')
    else:
        form = SightingsForm(instance=squirrel)

    context = {
        'form': form,
    }
