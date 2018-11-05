from django.contrib import admin

# Register your models here.
from PUPG.models import Person, Pet

admin.site.register(Person)
admin.site.register(Pet)
