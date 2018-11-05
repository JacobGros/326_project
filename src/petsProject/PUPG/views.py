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
    return render(request, "index.html", context=context)
    context = {
            "num_pets": num_pets,
            }

def submit(request):
    num_pets = Pet.objects.all().count()
    return render(request, "index.html", context=context)
    conext = {
            "num_pets": num_pets,
            }

class petsview(generic.ListView):
    model = Pet
    
