import os

def populate():
    python_pet = add_pet('Python')

    add_pet(pet=python_pet,
        name="Fred",
        animal_breed="Dog",
        pid= 4,
        vote_count= 24,
        age= 2
        )

    add_pet(pet=python_pet,
        name="Bob",
        animal_breed="Dog",
        pid= 5,
        vote_count= 26,
        age= 1
        )

    add_pet(pet=python_pet,
        name="Randy",
        animal_breed="Cat",
        pid= 2,
        vote_count= 20,
        age= 3
        )

    django_pet = add_pet("Django")

    add_pet(pet=django_pet,
        name="Randy",
        animal_breed="Cat",
        pid= 2,
        vote_count= 20,
        age= 3
        )

    add_pet(cat=django_cat,
        name="Bob",
        animal_breed="Dog",
        pid= 5,
        vote_count= 26,
        age= 1
        )

    add_pet(cat=django_cat,
        name="Fred",
        animal_breed="Dog",
        pid= 4,
        vote_count= 24,
        age= 2
        )

    # Print out what we have added to the user.
    for c in Category.objects.all():
        #print(c) 
        for p in Pet.objects.filter(category==c):
           print( "- {0} - {1}".format(str(c), str(p)))

def add_pet(pup, animal_breed, pid, vote_count, age):
    p = Pet.objects.get_or_create(category=pup, animal_breed=animal_breed, pid=pid, vote_count=vote_count)[0]
    return p

def add_pup(name):
    c = Category.objects.get_or_create(name=name)[0]
    return c

# Start execution here!
if __name__ == '__main__':
    print ("Starting PUPG population script...")
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'petsProject.settings')
    from PUPG.models import User, Pet
    populate()
