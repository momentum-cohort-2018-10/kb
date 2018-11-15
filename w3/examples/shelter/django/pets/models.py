from django.db import models


# Create your models here.
class Dog(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    description = models.CharField(max_length=255, null=False, blank=False)
    img_filename = models.CharField(max_length=50, null=True, blank=True)
    age = models.CharField(
        max_length=10,
        null=False,
        blank=False,
        choices=(
            ('puppy', 'Puppy'),
            ('young', 'Young'),
            ('adult', 'Adult'),
            ('senior', 'Senior'),
        ))
    size = models.IntegerField(
        null=False,
        blank=False,
        choices=(
            (1, 'Tiny'),
            (2, 'Small'),
            (3, 'Medium'),
            (4, 'Large'),
        ))
    good_with_kids = models.BooleanField(default=False)
    good_with_dogs = models.BooleanField(default=False)
    good_with_cats = models.BooleanField(default=False)

    def __str__(self):
        return self.name
