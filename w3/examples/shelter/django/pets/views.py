from django.shortcuts import render
from pets.models import Dog

# Create your views here.


def index(request):
    dogs = Dog.objects.all()
    response = render(request, 'pets/index.html', {
        "shelter_name": "Lazy River Shelter",
        "dogs": dogs,
    })
    return response


def dog(request, dog_id):
    dog = Dog.objects.get(pk=dog_id)
    response = render(request, 'pets/dog.html', {
        "shelter_name": "Lazy River Shelter",
        "dog": dog,
    })
    return response


def contact(request):
    return render(request, "pets/contact.html", {
        "shelter_name": "Lazy River Shelter",
    })
