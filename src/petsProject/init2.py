import random
from faker import Faker
from io import BytesIO
from PUPG.models import Pet, User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.files.base import ContentFile
from PIL import Image

fake = Faker()

species = ["Dog", "Cat", "Mouse", "Hampster", "Lizard", "Snake", "Fish", "Snail", "Horse", "Rock", "Chinchilla", "Chicken",
        "Bird", "Frog"]
 

users = []
for x in range(300):
    user = User(name = fake.first_name() + " " + fake.last_name(), User_id = x, pet_id = 123,  username = fake.text(25).replace(" ", ""),  password = fake.text(25).replace(" ", ""),  age = 36, country = "USA" )
    users.append(user)
    user.save()

for x in range(400):
    
    s = random.randint(0,13)
    u = random.randint(0,299)
    pic = random.randint(1,15)

    img  = Image.open("media/" + str(pic) + ".jpg")
    thumb_io = BytesIO()
    img.save(thumb_io, img.format, quality=90)

    pet = Pet(name = fake.first_name(), animal_type = species[s], animal_breed = "unknown", pid = x, vote_count = random.randint(0,1000), pet_owner = users[u],
            age = random.randint(1,15))

    pet.picture.save(img.filename, ContentFile(thumb_io.getvalue()), save=False)



    pet.save()


print('All Pet Instances: ')
for pet in Pet.objects.all():
    print(pet)


print('All User Instances: ')
for user in User.objects.all():
    print(user)



for user in User.objects.all():
    print("")
    print(user.name + " pets: ")
    for p in Pet.objects.all():
        if p.pet_owner == user:
            print(p)
    print("")


