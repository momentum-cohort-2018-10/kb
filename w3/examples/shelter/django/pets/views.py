from django.shortcuts import render
from pets.dogs import dogs

# Create your views here.


def index(request):
    return render(request, 'pets/index.html', {
        "shelter_name": "Lazy River Shelter",
        "dogs": dogs,
    })
