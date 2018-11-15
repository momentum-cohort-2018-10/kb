from django.contrib import admin
from pets.models import Dog


# Register your models here.
class DogAdmin(admin.ModelAdmin):
    model = Dog
    list_display = (
        'name',
        'description',
        'age',
    )


admin.site.register(Dog, DogAdmin)
