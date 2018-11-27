import random
from faker import Faker
from io import BytesIO
from PUPG.models import Pet, Person
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.files.base import ContentFile
from PIL import Image
from django.contrib.auth.models import User


fake = Faker()

species = ["Dog", "Cat", "Mouse", "Hampster", "Lizard", "Snake", "Fish", "Snail", "Horse", "Rock", "Chinchilla", "Chicken",
        "Bird", "Frog"]
 

users = []
for x in range(150):
    user = Person(name = fake.first_name() + " " + fake.last_name(), username = fake.text(25).replace(" ", ""),  password = fake.text(25).replace(" ", ""), country = "USA" )
    users.append(user)
    user.save()

for x in range(200):
    
    s = random.randint(0,13)
    u = random.randint(0,149)
    pic = random.randint(1,15)

    img  = Image.open("media/" + str(pic) + ".jpg")
    thumb_io = BytesIO()
    img.save(thumb_io, img.format, quality=90)

    pet = Pet(name = fake.first_name(), animal_type = species[s], animal_breed = "unknown", pid = x, vote_count = random.randint(0,1000), pet_owner = users[u],
            age = random.randint(1,15))

    pet.picture.save(img.filename, ContentFile(thumb_io.getvalue()), save=True)



    pet.save()


print('All Pet Instances: ')
for pet in Pet.objects.all():
    print(pet)


print('All Person Instances: ')
for user in Person.objects.all():
    print(user)



for user in Person.objects.all():
    print("")
    print(user.name + " pets: ")
    for p in Pet.objects.all():
        if p.pet_owner == user:
            print(p)
    print("")

#regular user
usern = "Harold"
pw = "moose_123"
em = "harold@326.edu"
reguser = User.objects.create_user(usern, em, pw)
reguser.save()





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



