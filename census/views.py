from django.shortcuts import render
from django.shortcuts import redirect

from django.shortcuts import redirect
from .models import Sightings

def index(request):
    return HttpResponse("It works!")

def map(request):
    address_points = Sightings.objects.all()
    address_latitude = []
    address_longitude = []
    address_data = []
    for squirrel in range(len(address_points)):
        address_latitude.append(address_points[i].Latitude)
        address_longitude.append(address_points[i].Longitude)
    for point in range(len(address_points)):
        L.marker([address_latitude[point],address_longitude[point]]).addTo(m)
    context = {'address_longitude': address_longitude,
            'address_latitude': address_latitude}
   # context = {'address_longitude': json.dumps(address_longitude),
    #        'address_latitude': json.dumps(address_latitude), 'address_data': json.dumps(address_data)}
    return render(request,'census/map.html',context)

# Create your views here.
