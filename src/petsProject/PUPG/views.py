from django.shortcuts import render

# Create your views here.

def index(request):

     num_pets = Pet.objects.all().count()
     num_people = Person.objects.all()count()


     context = {
            "num_pets": num_pets,
            "num_people": num_people,
            }

     return render(request, "index.html", context=context)
