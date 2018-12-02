

import random
from faker import Faker
from io import BytesIO
from PUPG.models import Pet, Person
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.files.base import ContentFile
from PIL import Image
from django.contrib.auth.models import User, Group, Permission 
from django.contrib.contenttypes.models import ContentType



fake = Faker()

species = ["Dog", "Cat", "Reptile", "Fish", "Bird", "Horse", "Small Mammal", "Rock",
        "Bug"]


moderatorGroup = Group()
moderatorGroup.name = 'moderators'
moderatorGroup.save()

ct = ContentType.objects.get_for_model(User)


permission1 = Permission.objects.create(codename='can_add_Pet',
                                   name='Can add pet', content_type=ct)


permission2 = Permission.objects.create(codename='can_delete_Pet',
                                   name='Can delete pet', content_type=ct)

permission3 = Permission.objects.create(codename='can_change_Pet',
                                   name='Can change pet', content_type=ct)

permission4 = Permission.objects.create(codename='can_add_User',
                                   name='Can add user', content_type=ct)

permission5 = Permission.objects.create(codename='can_delete_User',
                                   name='Can delete user', content_type=ct)

moderatorGroup.permissions.add(permission1)
moderatorGroup.permissions.add(permission2)
moderatorGroup.permissions.add(permission3)
moderatorGroup.permissions.add(permission4)
moderatorGroup.permissions.add(permission5)

users = []


print("GENERATING USERS:")

for x in range(150):

    fname = fake.first_name()
    lname = fake.last_name()
    usern = fname+fake.text(6).replace(".", "").replace(" ", "") + str(random.randint(1,10000))
    pw = fake.text(10).replace(" ","").replace(".", "")
    em = usern+"@326.edu"
    reguser = User.objects.create_user(usern, em, pw)
    reguser.save()
    reguser.first_name = fname
    reguser.last_name = lname
    reguser.person.name = reguser.first_name + " " + reguser.last_name
    reguser.person.country = "USA"
    reguser.person.votes_given = random.randint(0,10000000)
    reguser.save() 
    users.append(reguser)
    print("Username: " + usern)
    print("Password: " + pw)
    print("Person's Name: " + reguser.person.name)
    print("votes given: " + str(reguser.person.votes_given))
    print(" ")


dogs = [1,10,11,12,2,4,32,33,34,35,55,56,57,58,122,123,124,125,126,127,128,129,130,131,140,141,142,143,144,145,]
cats = [13,14,5,68,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,]
birds = [15,21,27,28,49,50,51,52,53,146,147,148,149,150,151,152,153,154,155,156,]
sm_mam = [3,6,25,29,63,64,65,66,67,69,138,139,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,]
bugs = [7,19,20,54,59,60,61,62,88,89,90,91,92,93,94,95,]
reptile = [8,18,26,31,36,37,38,39,132,133,134,135,136,137,175,176,177,178,179,180,]
rock = [9,22,23,24,]
fish = [17,30,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,]
horse = [16,40,41,42,43,44,45,46,47,48,181,182,183,184,185,186,187,188,189,190,]

def add_specific_pet(name, species, age, pic, Image, BytesIO, Pet, random, ContentFile, users):
    u = random.randint(0,149)
    img  = Image.open("media/" + str(pic) + ".jpg")
    thumb_io = BytesIO()
    img.save(thumb_io, img.format, quality=90)

    pet = Pet(name = name, animal_type = species, vote_count = random.randint(0,1000), pet_owner = users[u].person,
            age = age)

    pet.picture.save(img.filename, ContentFile(thumb_io.getvalue()), save=True)


    pet.save()

    print("Pet " + pet.name + " who is a " + pet.animal_type + " has been assigned to " + users[u].person.name + "!")


for x in range(200):

    s = random.randint(0,8)
    u = random.randint(0,149)
    pic = random.randint(1,139)
    
    if pic in dogs:
        s = 0
    if pic in cats:
        s = 1
    if pic in birds:
        s = 4
    if pic in sm_mam:
        s = 6
    if pic in bugs:
        s = 8
    if pic in reptile:
        s = 2
    if pic in rock:
        s = 7
    if pic in fish:
        s = 3
    if pic in horse:
        s = 5


    img  = Image.open("media/" + str(pic) + ".jpg")
    thumb_io = BytesIO()
    img.save(thumb_io, img.format, quality=90)

    pet = Pet(name = fake.first_name(), animal_type = species[s], vote_count = random.randint(0,1000), pet_owner = users[u].person,
            age = random.randint(1,15))

    pet.picture.save(img.filename, ContentFile(thumb_io.getvalue()), save=True)




    pet.save()

    print("Pet " + pet.name + " who is a " + pet.animal_type + " has been assigned to " + users[u].person.name + "!")


add_specific_pet("Lola", "Cat", 9, "lola", Image, BytesIO, Pet, random, ContentFile, users)
add_specific_pet("Cinnabon", "Small Mammal", 5, "cinnabon", Image, BytesIO, Pet, random, ContentFile, users)
add_specific_pet("Nacho", "Dog", 4, "nacho", Image, BytesIO, Pet, random, ContentFile, users)

username = "admin"
password = "admin"
email = "admin@326.edu"
adminuser = User.objects.create_user(username, email, password)
adminuser.save()
fname = fake.first_name()
lname = fake.last_name()

adminuser.first_name = fname
adminuser.last_name = lname
adminuser.person.name = reguser.first_name + " " + reguser.last_name
adminuser.person.country = "USA"
adminuser.person.votes_given = 0 


adminuser.is_superuser = True
adminuser.is_staff = True
adminuser.save()

moderatorGroup.user_set.add(adminuser)


message = f"""
====================================================================
The database has been setup with the following credentials:

  username: {username}
  password: {password}
  email: {email}

You will need to use the username {username} and password {password}
to login to the administrative webapp in Django.

Please visit http://localhost:8080/admin to login to the admin app.
Run the django server with:

  $ python3 manage.py runserver 0.0.0.0:8080
====================================================================
"""
print(message)



print("yeah")  
