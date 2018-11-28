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
    #animal_breed = models.CharField(max_length=20, help_text='Enter Breed')
    pid = models.IntegerField()
    vote_count = models.IntegerField()
    pet_owner = models.ForeignKey('Person', on_delete=models.SET_NULL, null = True)
    #pet_owner = models.CharField(max_length=20, help_text='Enter Owner ID')
    age = models.IntegerField()
    picture = models.ImageField(max_length = 255) 
    
    def get_absolute_url(self):
        return reverse("pet-detail", args=[str(self.id)])


    def __str__(self):
        return "Name:  "+ self.name +  "     Picture: " + self.picture.name + "     Species: " + self.animal_type + "     Vote Count: " + str(self.vote_count)
    

class Person(models.Model):
    name = models.CharField(max_length=20, help_text='Enter Name')
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    #username = models.CharField(max_length=20, help_text='Enter Username')
    #password = models.CharField(max_length=20, help_text='Enter Password')
    #age = models.IntegerField(null=True, blank=True)
    country = models.CharField(max_length=20, help_text='Enter Country')
   
    @receiver(post_save, sender=User)
    def update_user_profile(sender, instance, created, **kwargs):
        if created:
            Person.objects.create(user=instance)
        instance.person.save()

    #@receiver(post_save, sender=User)
    #def create_user_person(sender, instance, created, **kwargs):
    #    if created:
    #        Person.objects.create(user=instance)

    #@receiver(post_save, sender=User)
    #def save_user_person(sender, instance, **kwargs):
    #    instance.person.save()


    def __str__(self):
        return "Name: " + self.name + " Username: " + self.user.username + " Password: " + self.user.password
     
    def get_absolute_url(self):
         return reverse("person-detail", args=[str(self.id)])

