from django.shortcuts import render
import random
from PUPG.models import Person, Pet
from django.views import generic
# Create your views here.

def index(request):

    num_pets = Pet.objects.all().count()
    num_people = Person.objects.all().count()


    ordered_pets = []

    for pet in Pet.objects.all().order_by('-vote_count'):
        ordered_pets.append(pet)

    

    context = {
            "num_pets": num_pets,
            "num_people": num_people,
            "winner": ordered_pets[0]
            "random pet": ordered_pets[random.randint(0,200)]
            }

    return render(request, "index.html", context=context)

def vote(request):
    num_pets = Pet.objects.all().count()
    num_people = Person.objects.all().count()
    
    x = random.randint(0, Pet.objects.all().count()-1)
    
    
    contender1 =  Pet.objects.all()[x]
    
    x = random.randint(0, Pet.objects.all().count()-1)

    contender2 =  Pet.objects.all()[x]


    while (contender1 == contender2):
        
        x = random.randint(0, Pet.objects.all().count()-1)
        contender2 =  Pet.objects.all()[x]


    

    context = {
                "c1": contender1,
                "c2": contender2,
                }

    return render(request, "versus.html", context=context)

def leaderboard(request):
    num_pets = Pet.objects.all().count()

    ordered_pets = []

    context = {
                "num_pets": num_pets,
                }

    
    for pet in Pet.objects.all().order_by('-vote_count'):
        ordered_pets.append(pet)

    #for x in range(len(ordered_pets)):
       # context = context+  {str(x+1) + "_place": ordered_pets[x] }
     #   context[str(x+1) + "_place"] = ordered_pets[x]
 
    context["ordered_pets"] = ordered_pets 


    return render(request, "leaderBoardDraft1.html", context=context)



def submit(request):
    num_pets = Pet.objects.all().count()
    context = {
            "num_pets": num_pets,
            }
    return render(request, "submit.html", context=context)

class PersonDetailView(generic.DetailView):
    model = Person
    template_name = "person_detail.html"

class PetDetailView(generic.DetailView):
    model = Pet
    template_name = "pet_detail.html"
