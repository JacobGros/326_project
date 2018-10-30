from django.contrib import admin

# Register your models here.
from PUPG.models import User, Pet

admin.site.register(User)
admin.site.register(Pet)
