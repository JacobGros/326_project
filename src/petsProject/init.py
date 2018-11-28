

import random
from faker import Faker
from io import BytesIO
from PUPG.models import Pet, Person
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.files.base import ContentFile
from PIL import Image
from django.contrib.auth.models import User


fake = Faker()

species = ["Dog", "Cat", "Reptile", "Fish", "Bird", "Horse", "Small Mammal", "Rock",
        "Bug"]


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
    reguser.save() 
    users.append(reguser)
    print("Username: " + usern)
    print("Password: " + pw)
    print("Person's Name: " + reguser.person.name)
    print(" ")


for x in range(200):

    s = random.randint(0,8)
    u = random.randint(0,149)
    pic = random.randint(1,15)
    
    dogs = [1,10,11,12,2,4,]
    cats = [13,14,5,]
    birds = [15,]
    sm_mam = [3,6,]
    bugs = [7,]
    reptile = [8,]
    rock = [9,]
    fish = []
    horse = []

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

    pet = Pet(name = fake.first_name(), animal_type = species[s], pid = x, vote_count = random.randint(0,1000), pet_owner = users[u].person,
            age = random.randint(1,15))

    pet.picture.save(img.filename, ContentFile(thumb_io.getvalue()), save=True)




    pet.save()

    print("Pet " + pet.name + " who is a " + pet.animal_type + " has been assigned to " + users[u].person.name + "!")


#pic = random.randint(1,15)

#img  = Image.open("media/" + str(pic) + ".jpg")
#thumb_io = BytesIO()
#img.save(thumb_io, img.format, quality=90)

##pet = Pet(name = fake.first_name(), animal_type = "dog", pid = 1, vote_count = random.randint(0,1000), pet_owner = users[0].person,
  #      age = random.randint(1,15))

#pet.picture.save(img.filename, ContentFile(thumb_io.getvalue()), save=True)



#pet.save()




username = "admin"
password = "admin"
email = "admin@326.edu"
adminuser = User.objects.create_user(username, email, password)
adminuser.save()
adminuser.is_superuser = True
adminuser.is_staff = True
adminuser.save()
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
