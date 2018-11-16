from django.contrib import admin
from pets.models import Dog, AdoptionApplication


# Register your models here.
class DogAdmin(admin.ModelAdmin):
    model = Dog
    list_display = (
        'name',
        'description',
        'age',
    )


class AdoptionApplicationAdmin(admin.ModelAdmin):
    model = AdoptionApplication
    list_display = (
        'dog',
        'name',
        'email',
    )


admin.site.register(Dog, DogAdmin)
admin.site.register(AdoptionApplication, AdoptionApplicationAdmin)
