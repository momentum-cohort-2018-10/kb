from django.db import models


# Create your models here.
class Dog(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    description = models.CharField(max_length=255, null=False, blank=False)
    picture = models.ImageField(upload_to='dogs/', null=True)
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
