from django.db import models
from django.urls import reverse
import uuid
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
SPECIES = (
	('Dog', 'Dog'), ('Cat', 'Cat'), ('Reptile', 'Reptile'), ('Fish', 'Fish'), ('Bird', 'Bird'), ('Horse', 'Horse'), ('Small Mammal', 'Small Mammal'), ('Rock', 'Rock'), ('Bug', 'Bug')
)
AGE = (
	(1,'1'), (2,'2'), (3,'3'), (4,'4'), (5,'5'), (6,'6'), (7,'7'), (8,'8'), (9,'9'), (10,'10'), (11,'11'), (12,'12'), (13,'13'), (14,'14'), (15,'15'), (16,'16'), (17,'17'), (18,'18'), (19,'19'), (20,'20'), (21,'21'), (22,'22'), (23,'23'), (24,'24'), (25,'25'), (26,'26'), (27,'27'), (28,'28'), (29,'29'), (30,'30'), (31,'31'), (32,'32'), (33,'33'), (34,'34'), (35,'35'), (36,'36'), (37,'37') 
)
class Pet(models.Model):

    name = models.CharField(max_length=20, help_text='Enter Name')
    animal_type = models.CharField(max_length=20, help_text='Enter Animal Type', choices=SPECIES)
    vote_count = models.IntegerField()
    pet_owner = models.ForeignKey('Person', on_delete=models.SET_NULL, null = True)
    age = models.IntegerField(choices=AGE)
    picture = models.ImageField('profile picture', upload_to = 'media/', max_length = 255, null = True) 
    
    def get_absolute_url(self):
        return reverse("pet-detail", args=[str(self.id)])


    def __str__(self):
        return "Name:  "+ self.name +  "     Picture: " + self.picture.name + "     Species: " + self.animal_type + "     Vote Count: " + str(self.vote_count)
    

class Person(models.Model):
    name = models.CharField(max_length=20, help_text='Enter Name')
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    country = models.CharField(max_length=20, help_text='Enter Country')
    votes_given = models.IntegerField(default=0)
    rank = models.CharField(max_length=50, default="Pet Amateur") 
    

    @receiver(post_save, sender=User)
    def update_user_profile(sender, instance, created, **kwargs):
        if created:
            Person.objects.create(user=instance)
        instance.person.save()

    def __str__(self):
        return "Name: " + self.name + " Username: " + self.user.username + " Password: " + self.user.password

    def assign_rank(self):
        if(self.votes_given >= 100000000000):
            self.rank = "Crazy Cat Lady [max level]"
        elif(self.votes_given >= 10000000):
            self.rank = "Divine Lover of Pets"
        elif(self.votes_given >= 3000000):
            self.rank = "Pet Devoted Worshipper"
        elif(self.votes_given >= 1000000 ):
            self.rank = "Pet Worshipper "
        elif(self.votes_given >= 500000  ):
            self.rank = "Pet Devotee"
        elif(self.votes_given >= 100000  ):
            self.rank = "Pet Enthusiast"
        elif(self.votes_given >= 50000  ):
            self.rank = "Pet Believer"
        elif(self.votes_given >= 25000  ):
            self.rank = " Pet Addict"
        elif(self.votes_given >= 15000  ):
            self.rank = "Pet Maniac"
        elif(self.votes_given >= 10000  ):
            self.rank = "Pet Fanatic"
        elif(self.votes_given >= 6000  ):
            self.rank = "Pet Extremist"
        elif(self.votes_given >= 3000  ):
            self.rank = "Pet Zealot"
        elif(self.votes_given >= 1750  ):
            self.rank = "Pet Aficionado"
        elif(self.votes_given >= 1000):
            self.rank = "Pet Lover"
        elif(self.votes_given >= 500):
            self.rank = "Pet Adorer"
        elif(self.votes_given >= 100):
            self.rank = "Pet Fan"
        else:
            self.rank = "Pet Amateur"




    def get_absolute_url(self):
         return reverse("person-detail", args=[str(self.id)])

