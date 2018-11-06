from django.shortcuts import render

from PUPG.models import Person, Pet
from django.views import generic
# Create your views here.

def index(request):

     num_pets = Pet.objects.all().count()
     num_people = Person.objects.all().count()


     context = {
            "num_pets": num_pets,
            "num_people": num_people,
            }

     return render(request, "index.html", context=context)



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
    return render(request, "index.html", context=context)
    conext = {
            "num_pets": num_pets,
            }

class petsview(generic.ListView):
    model = Pet
    
