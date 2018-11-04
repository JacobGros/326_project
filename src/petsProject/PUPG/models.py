from django.db import models

# Create your models here.
class Pet(models.Model):

    name = models.CharField(max_length=20, help_text='Enter Name')
    animal_type = models.CharField(max_length=20, help_text='Enter Animal Type')
    animal_breed = models.CharField(max_length=20, help_text='Enter Breed')
    pid = models.IntegerField()
    vote_count = models.IntegerField()
    pet_owner = models.ForeignKey('User', on_delete=models.SET_NULL, null = True)
    #pet_owner = models.CharField(max_length=20, help_text='Enter Owner ID')
    age = models.IntegerField()
    #image = models.ImageField(upload_to = this.pid) 



    def __str__(self):
        return "Name:  "+ self.name + "     Species: " + self.animal_type + "     Vote Count: " + str(self.vote_count)
    

class User(models.Model):
    name = models.CharField(max_length=20, help_text='Enter Name')
    User_id = models.IntegerField()
    pet_id = models.IntegerField()
    username = models.CharField(max_length=20, help_text='Enter Username')
    password = models.CharField(max_length=20, help_text='Enter Password')
    age = models.IntegerField()
    country = models.CharField(max_length=20, help_text='Enter Country')


    def __str__(self):
        return "Name: " + self.name + " Username: " + self.username + " Password: " + self.password
