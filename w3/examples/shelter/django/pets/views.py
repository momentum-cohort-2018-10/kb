from django.shortcuts import render
from pets.dogs import dogs

# Create your views here.


def index(request):
    response = render(request, 'pets/index.html', {
        "shelter_name": "Lazy River Shelter",
        "dogs": dogs,
    })
    return response


def contact(request):
    return render(request, "pets/contact.html", {
        "shelter_name": "Lazy River Shelter",
    })
