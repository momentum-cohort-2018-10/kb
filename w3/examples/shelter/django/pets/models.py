from django.db import models
from localflavor.us.models import USStateField, USZipCodeField

DOG_AGE_CHOICES = (
    ('puppy', 'Puppy'),
    ('young', 'Young'),
    ('adult', 'Adult'),
    ('senior', 'Senior'),
)

DOG_SIZE_CHOICES = (
    (1, 'Tiny'),
    (2, 'Small'),
    (3, 'Medium'),
    (4, 'Large'),
)


# Create your models here.
class Dog(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    description = models.CharField(max_length=255, null=False, blank=False)
    picture = models.ImageField(upload_to='dogs/', null=True)
    age = models.CharField(
        max_length=10, null=False, blank=False, choices=DOG_AGE_CHOICES)
    size = models.IntegerField(
        null=False, blank=False, choices=DOG_SIZE_CHOICES)
    good_with_kids = models.BooleanField(default=False)
    good_with_dogs = models.BooleanField(default=False)
    good_with_cats = models.BooleanField(default=False)

    def get_qualities(self):
        qualities = []
        qualities.append(self.get_age_display())
        qualities.append(self.get_size_display())
        if self.good_with_kids:
            qualities.append("Good with kids")
        if self.good_with_dogs:
            qualities.append("Good with other dogs")
        if self.good_with_cats:
            qualities.append("Good with cats")
        return qualities

    def __str__(self):
        return self.name


class AdoptionApplication(models.Model):
    dog = models.ForeignKey(to='Dog', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    current_pet_owner = models.BooleanField()
    phone_number = models.CharField(max_length=30)
    address1 = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255)
    state = USStateField()
    zip = USZipCodeField()

    def __str__(self):
        return f"{self.dog} - {self.name}"
