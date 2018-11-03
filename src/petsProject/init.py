import os

def populate():
    

    add_pet(name="Fred",
        animal_breed="Dog",
        pid= 4,
        vote_count= 24,
        age= 2
        )

    add_pet(name="Bob",
        animal_breed="Dog",
        pid= 5,
        vote_count= 26,
        age= 1
        )

    add_pet(name="Randy",
        animal_breed="Cat",
        pid= 2,
        vote_count= 20,
        age= 3
        )

    add_pet(name="Randy",
        animal_breed="Cat",
        pid= 2,
        vote_count= 20,
        age= 3
        )

    add_pet(name="Bob",
        animal_breed="Dog",
        pid= 5,
        vote_count= 26,
        age= 1
        )

    add_pet(name="Fred",
        animal_breed="Dog",
        pid= 4,
        vote_count= 24,
        age= 2
        )

    # Print out what we have added to the user.
    for c in User.objects.all():
        #print(c) 
        for p in Pet.objects.filter(user==c):
           print( "- {0} - {1}".format(str(c), str(p)))

def add_pet(name, animal_type, animal_breed, pid, vote_count, pet_owner, age):
    p = Pet.objects.get_or_create(name=name, animal_type=animal_type, animal_breed=animal_breed, pid=pid, vote_count=vote_count, pet_owner=pet_owner, age=age)[0]
    return p

def add_user(name, User_id, pet_id, username, age, country):
    c = User.objects.get_or_create(name=name, User_id=User_id, pet_id=pet_id, username=username, age=age, country=country)[0]
    return c

# Start execution here!
if __name__ == '__main__':
    print ("Starting PUPG population script...")
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'petsProject.settings')
    from PUPG.models import User, Pet
    populate()
