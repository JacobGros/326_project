from django.db import models

# Create your models here.
class Pet(models.Model):

    name = models.CharField(max_length=20, help_text='Enter Name')
    animal_type = models.CharField(max_length=20, help_text='Enter Animal Type')
    animal_breed = models.CharField(max_length=20, help_text='Enter Breed')
    pet_id = models.IntegerField()
    vote_count = models.IntegerField()


