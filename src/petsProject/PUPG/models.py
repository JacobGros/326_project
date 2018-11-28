from django.db import models
from django.urls import reverse
import uuid
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Pet(models.Model):

    name = models.CharField(max_length=20, help_text='Enter Name')
    animal_type = models.CharField(max_length=20, help_text='Enter Animal Type')
    vote_count = models.IntegerField()
    pet_owner = models.ForeignKey('Person', on_delete=models.SET_NULL, null = True)
    age = models.IntegerField()
    picture = models.ImageField(max_length = 255) 
    
    def get_absolute_url(self):
        return reverse("pet-detail", args=[str(self.id)])


    def __str__(self):
        return "Name:  "+ self.name +  "     Picture: " + self.picture.name + "     Species: " + self.animal_type + "     Vote Count: " + str(self.vote_count)
    

class Person(models.Model):
    name = models.CharField(max_length=20, help_text='Enter Name')
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    country = models.CharField(max_length=20, help_text='Enter Country')
   
    @receiver(post_save, sender=User)
    def update_user_profile(sender, instance, created, **kwargs):
        if created:
            Person.objects.create(user=instance)
        instance.person.save()

    def __str__(self):
        return "Name: " + self.name + " Username: " + self.user.username + " Password: " + self.user.password
     
    def get_absolute_url(self):
         return reverse("person-detail", args=[str(self.id)])

