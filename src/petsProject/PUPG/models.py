from django.db import models

# Create your models here.
class Pet(models.Model):

    name = models.CharField(max_length=20, help_text='Enter Name')
    animal_type = models.CharField(max_length=20, help_text='Enter Animal Type')
    animal_breed = models.CharField(max_length=20, help_text='Enter Breed')
    pid = models.IntegerField()
    vote_count = models.IntegerField()
    pet_owner = models.CharField(max_length=20, help_text='Enter Owner ID')
    age = models.IntegerField()
    vote_count  = models.IntegerField()

class User(models.Model):
    name = models.CharField(max_length=20, help_text='Enter Name')
    User_id = models.IntegerField()
    pet_id = models.IntegerField()
    username = models.CharField(max_length=20, help_text='Enter Username')
    age = models.IntegerField()
    country = models.CharField(max_length=20, help_text='Enter Country')
