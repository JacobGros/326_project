import random
from PUPG.models import Person, Pet
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from PUPG.forms import SignUpForm, UserForm, PersonForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from django.contrib import messages
from difflib import SequenceMatcher
from django.contrib.auth.models import User


# Create your views here.
def index(request):

    num_pets = Pet.objects.all().count()
    num_people = Person.objects.all().count()


    ordered_pets = []

    for pet in Pet.objects.all().order_by('-vote_count'):
        ordered_pets.append(pet)

    x = random.randint(1,(num_pets-1))

    random_pet = ordered_pets[x]


    verbs = ['invented','specializes in', 'wrote a book on', 'lectures on', 'owns', 'wants', 'obsesses over', 'studies', 'likes', 'eats', 'despises', 'prefers', 'enjoys the presence of', 'hates', 'loves',   ]

    nouns = ['the works of William Shakespeare', 'pancakes', 'Robert Frost poems', 'cookies', 'computers', 'new shoes', 'designer brands', 'historical art', 'ice cream', 'money', 'clothes', 'mail', 'books', 'phones', 'classical music', 'science textbooks', 'math books', 'Lamborghinis', 'private yachts', 'limos', 'private jets', 'gold', 'candy', 'pickles']

    awards = ['Best Snuggles', 'Strongest Pet', 'Most Successful Pet', 'Best Laugh', 'Best Smile', 'Most Athletic Pet', 'Best Dancer', 'Most Spirited Pet','Most Clumsy Pet','Bravest Pet','Smartest Pet','Busiest Pet','Most Productive Pet', 'Cleanest Pet', 'Most Optimistic Pet'
            ]

    r1 = random.randint(0,1)
    random_sentence = ""

    if r1 == 0:
        random_sentence = random_pet.name + " " + verbs[random.randint(0,len(verbs)-1)] + " " + nouns[random.randint(0,len(nouns)-1)] + "!" 

    if r1 == 2:
        random_sentence = random_pet.name + " recently won the " + awards[random.randint(0,len(awards)-1)] + " Award!"

    context = {
            "num_pets": num_pets,
            "num_people": num_people,
            "winner": ordered_pets[0],
            "random_pet": ordered_pets[x],
            "random_sentence": random_sentence,
            }

    print(random_sentence)


    if request.user.is_authenticated:
        user = request.user
        person = user.person
        context["person"] = person


    return render(request, "index.html", context=context)

@login_required
def vote(request):

    user = request.user

    num_pets = Pet.objects.all().count()
    num_people = Person.objects.all().count()
    
    x = random.randint(0, Pet.objects.all().count()-1)
    
    
    contender1 =  Pet.objects.all()[x]

    while(contender1.pet_owner == user.person):
        x = random.randint(0, Pet.objects.all().count()-1)
        contender1 =  Pet.objects.all()[x]

    
    x = random.randint(0, Pet.objects.all().count()-1)

    contender2 =  Pet.objects.all()[x]


    while (contender1 == contender2 or contender2.pet_owner == user.person):
        
        x = random.randint(0, Pet.objects.all().count()-1)
        contender2 =  Pet.objects.all()[x]


    

    context = {
                "c1": contender1,
                "c2": contender2,
                }





    if request.user.is_authenticated:
        user = request.user
        person = user.person
        context["person"] = person

    return render(request, "versus.html", context=context)

def vote_for_pet(request, id):
    user = request.user
    user.person.votes_given +=1
    user.save()

    pet = Pet.objects.get(id=id)
    pet.vote_count += 1
    pet.save()
    return HttpResponseRedirect('/PUPG/vote/')


def leaderboardSpecies(request):

    context = {} 

    sort_by = request.GET.get('sort_by', None)
   
    message = ""

    dogs =  Pet.objects.all().filter(animal_type = "Dog")
    cats = Pet.objects.all().filter(animal_type = "Cat")
    reptiles = Pet.objects.all().filter(animal_type = "Reptile")
    fish = Pet.objects.all().filter(animal_type = "Fish")
    birds = Pet.objects.all().filter(animal_type = "Bird")
    horses = Pet.objects.all().filter(animal_type = "Horse")
    sm_mams = Pet.objects.all().filter(animal_type = "Small Mammal")
    rocks = Pet.objects.all().filter(animal_type = "Rock")
    bugs = Pet.objects.all().filter(animal_type = "Bug")
    
    tups = []
    dv = 0
    cv = 0
    rv = 0
    fv = 0
    bv = 0
    hv = 0
    sv = 0
    rov = 0
    biv = 0

    nd = 0
    nc = 0
    nr = 0
    nf = 0
    nb = 0
    nh = 0
    ns = 0
    nro = 0
    nbi = 0


    for pet in dogs:
        dv = dv + pet.vote_count
        nd = nd + 1
    for pet in cats:
        cv = cv + pet.vote_count
        nc = nc + 1
    for pet in reptiles:
        rv = rv + pet.vote_count
        nr = nr+1
    for pet in fish:
        fv = fv + pet.vote_count
        nf = nf+1
    for pet in horses:
        hv = hv + pet.vote_count
        nh = nh+1
    for pet in sm_mams:
        sv = sv + pet.vote_count
        ns = ns+1
    for pet in rocks:
        rov = rov + pet.vote_count
        nro = nro +1
    for pet in bugs:
        bv = bv + pet.vote_count
        nb = nb+1
    for pet in birds:
        biv = biv + pet.vote_count
        nbi = nbi+1
    dt = ("Dogs", dv, nd)
    ct = ("Cats",cv, nc)
    rt = ("Reptiles", rv, nr)
    ft = ("Fish",fv, nf)
    ht = ("Horses", hv, nh)
    st = ("Small Mammals",sv, ns)
    rot = ("Rocks", rov, nro)
    bt = ("Bugs",bv, nb)
    bit = ("Birds", biv, nbi)

    tups.append(dt)
    tups.append(ct)
    tups.append(rt)
    tups.append(ft)
    tups.append(bt)
    tups.append(ht)
    tups.append(st)
    tups.append(rot)
    tups.append(bit)

    def takeSecond(elem):
        return elem[1]
    def takeThird(elem):
        return elem[2]

    if(not sort_by or sort_by == "votes"):
        tups.sort(reverse = True, key=takeSecond)
        message = "Sorting by Number of Votes"

    else:
        tups.sort(reverse = True, key=takeThird)
        message = "Sorting by Number of Submissions"

    context["tups"] = tups
    context["m"] = message
    return render(request, "leaderBoardSpecies.html", context=context)


def leaderboard(request):

    num_pets = Pet.objects.all().count()

    ordered_pets = []

    context = {
                "num_pets": num_pets,
                }
    
    
    
    filtered_string = "Displaying: "
    
    showAll = request.GET.get('showAll', None)
    showDogs = request.GET.get('showDogs', None)
    showReptiles = request.GET.get('showReptiles', None)
    showFish = request.GET.get('showFish', None)
    showBirds = request.GET.get('showBirds', None)
    showHorse = request.GET.get('showHorse', None)
    showSM = request.GET.get('showSM', None)
    showRocks = request.GET.get('showRocks', None)
    showBugs = request.GET.get('showBugs', None)
    showCats = request.GET.get('showCats', None)
    
    pets = False 

    if((not showAll and not showDogs and not showCats and not showReptiles and not showFish and not showBirds and not showHorse and not  showSM and not showRocks and not showBugs) or showAll):
        pets = Pet.objects.all().order_by('-vote_count')
        filtered_string = filtered_string + "All Species  "

    else:
        if(showDogs):
            pets = Pet.objects.all().filter(animal_type = "Dog")
            filtered_string = filtered_string + "Dogs, "
        if(showCats):
            if(pets):
                pets = pets.union(Pet.objects.all().filter(animal_type = "Cat"))
            else:
                pets = Pet.objects.all().filter(animal_type = "Cat")
            filtered_string = filtered_string + "Cats, "

        if(showReptiles):
            if(pets):
                pets = pets.union(Pet.objects.all().filter(animal_type = "Reptile"))
            else:
                pets = Pet.objects.all().filter(animal_type = "Reptile")
            filtered_string = filtered_string + "Reptiles, "
        if(showFish):
            if(pets):
                pets = pets.union(Pet.objects.all().filter(animal_type = "Fish"))
            else:
                pets = Pet.objects.all().filter(animal_type = "Fish")
            filtered_string = filtered_string + "Fish, "
        if(showBirds):
            if(pets):
                pets = pets.union(Pet.objects.all().filter(animal_type = "Bird"))
            else:
                pets = Pet.objects.all().filter(animal_type = "Bird")
            filtered_string = filtered_string + "Birds, "
        if(showHorse):
            if(pets):
                pets = pets.union(Pet.objects.all().filter(animal_type = "Horse"))
            else:
                pets = Pet.objects.all().filter(animal_type = "Horse")
            filtered_string = filtered_string + "Horses, "
        if(showSM):
            if(pets):
                pets = pets.union(Pet.objects.all().filter(animal_type = "Small Mammal"))
            else:
                pets = Pet.objects.all().filter(animal_type = "Small Mammal")
            filtered_string = filtered_string + "Small Mammals, "
        if(showRocks):
            if(pets):
                pets = pets.union(Pet.objects.all().filter(animal_type = "Rock"))
            else:
                pets = Pet.objects.all().filter(animal_type = "Rock")
            filtered_string = filtered_string + "Rocks, "
        if(showBugs):
            if(pets):
                pets = pets.union(Pet.objects.all().filter(animal_type = "Bug"))
            else:
                pets = Pet.objects.all().filter(animal_type = "Bug")
            filtered_string = filtered_string + "Bugs, "
                
    
    filtered_string = filtered_string[0:len(filtered_string)-2] 
    pets = pets.order_by('-vote_count')
    
    for pet in pets:
        ordered_pets.append(pet)
    context["ordered_pets"] = ordered_pets 
    context["filtered_string"] = filtered_string 


    if request.user.is_authenticated:
        user = request.user
        person = user.person
        context["person"] = person

    return render(request, "leaderBoardDraft1.html", context=context)


class PetCreateView(LoginRequiredMixin, generic.CreateView):
    model = Pet
    template_name = "submit.html"
    fields = ['name', 'age', 'animal_type', 'picture']
    #fields = '__all__'
    
    

    def form_valid(self, form):
        form.instance.pet_owner = self.request.user.person
        form.instance.vote_count = '0'
        return super(PetCreateView, self).form_valid(form)

class PersonDetailView(generic.DetailView):
    model = Person
    template_name = "person_detail.html"
    rank = "Pet Amatuer" 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pets = [] 
        profile_votes = 0
        for pet in Pet.objects.all().filter(pet_owner = context['object']):
            pets.append(pet)
            profile_votes = profile_votes + pet.vote_count

        context['pets'] = pets
        context['votes'] = profile_votes
        context['votes_given'] = context['object'].votes_given


        if(context['object'].votes_given >= 100000000000):
            rank = "Crazy Cat Lady [max level]"
        elif(context['object'].votes_given >= 10000000):
            rank = "Divine Lover of Pets"
        elif(context['object'].votes_given >= 3000000):
            rank = "Pet Devoted Worshipper"
        elif(context['object'].votes_given >= 1000000 ):
            rank = "Pet Worshipper "
        elif(context['object'].votes_given >= 500000  ):
            rank = "Pet Devotee"
        elif(context['object'].votes_given >= 100000  ):
            rank = "Pet Enthusiast"
        elif(context['object'].votes_given >= 50000  ):
            rank = "Pet Believer"
        elif(context['object'].votes_given >= 25000  ):
            rank = " Pet Addict"
        elif(context['object'].votes_given >= 15000  ):
            rank = "Pet Maniac"
        elif(context['object'].votes_given >= 10000  ):
            rank = "Pet Fanatic"
        elif(context['object'].votes_given >= 6000  ):
            rank = "Pet Extremist"
        elif(context['object'].votes_given >= 3000  ):
            rank = "Pet Zealot"
        elif(context['object'].votes_given >= 1750  ):
            rank = "Pet Aficionado"
        elif(context['object'].votes_given >= 1000):
            rank = "Pet Lover"
        elif(context['object'].votes_given >= 500):
            rank = "Pet Adorer"
        elif(context['object'].votes_given >= 100):
            rank = "Pet Fan"
        else:
            rank = "Pet Amateur"



        context['rank'] = rank
        print(context['votes_given'])
        return context 



class PetDetailView(generic.DetailView):
    model = Pet
    template_name = "pet_detail.html"

def registration(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
             user = form.save()
             user.refresh_from_db()
             user.person.name = form.cleaned_data.get('first_name') + ' ' + form.cleaned_data.get('last_name')
             user.person.country = form.cleaned_data.get('country')
             user.save()
             raw_password = form.cleaned_data.get('password1')
             user = authenticate(username=user.username, password=raw_password)
             login(request, user)
             return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'registration/registration.html', {'form': form})

@login_required	
def my_profile(request):
    user = request.user
    person = user.person
    context= {}
    context['person'] = person
    pets = [] 
    profile_votes = 0
    for pet in Pet.objects.all().filter(pet_owner = context['person']):
        pets.append(pet)
        profile_votes = profile_votes + pet.vote_count
    context['pets'] = pets
    context['votes'] = profile_votes
    context['votes_given'] = context['person'].votes_given
	
    if(context['person'].votes_given >= 100000000000):
        rank = "Crazy Cat Lady [max level]"
    elif(context['person'].votes_given >= 10000000):
        rank = "Divine Lover of Pets"
    elif(context['person'].votes_given >= 3000000):
        rank = "Pet Devoted Worshipper"
    elif(context['person'].votes_given >= 1000000 ):
        rank = "Pet Worshipper "
    elif(context['person'].votes_given >= 500000  ):
        rank = "Pet Devotee"
    elif(context['person'].votes_given >= 100000  ):
        rank = "Pet Enthusiast"
    elif(context['person'].votes_given >= 50000  ):
        rank = "Pet Believer"
    elif(context['person'].votes_given >= 25000  ):
        rank = " Pet Addict"
    elif(context['person'].votes_given >= 15000  ):
        rank = "Pet Maniac"
    elif(context['person'].votes_given >= 10000  ):
        rank = "Pet Fanatic"
    elif(context['person'].votes_given >= 6000  ):
        rank = "Pet Extremist"
    elif(context['person'].votes_given >= 3000  ):
        rank = "Pet Zealot"
    elif(context['person'].votes_given >= 1750  ):
        rank = "Pet Aficionado"
    elif(context['person'].votes_given >= 1000):
        rank = "Pet Lover"
    elif(context['person'].votes_given >= 500):
        rank = "Pet Adorer"
    elif(context['person'].votes_given >= 100):
        rank = "Pet Fan"
    else:
        rank = "Pet Amateur"

    context['rank'] = rank
    return render(request, "profile_detail.html", context=context)
	
@login_required
def update_profile(request):
    if request.method == 'POST':
        #user_form = UserForm(request.POST, instance=request.user)
        person_form = PersonForm(request.POST, instance=request.user.person)
        if person_form.is_valid():# and user_form.is_valid():
            #user_form.save()
            person_form.save()
    else:
        #user_form = UserForm(instance=request.user)
        person_form = PersonForm(instance=request.user.person)
    
    if request.user.is_authenticated:
        user = request.user
        person = user.person


    context = {'person_form':person_form,'person':person,}
    #context = {'user_form':user_form,}# 'person':person,}
    return render(request, 'registration/profile.html', context=context)





def search_view(request):
  
    if request.method == 'GET': # If the form is submitted
        search_query = request.GET.get('search_box', None)

        models = request.GET.get('models', None)


        if(models == "Owners"): 
            users = User.objects.all()
            context = { 'search' : search_query} 
            user_tuples = []
            ordered_users = []
            profile_votes = []
            num_pets = []
            
            def nameMatch(search, u):
                return SequenceMatcher(None, search, u.person.name).ratio()

            for user in users:
                user_tuples.append((user, nameMatch(search_query, user)))

            def takeSecond(elem):
                return elem[1]

            user_tuples.sort(reverse = True, key=takeSecond)

            for u  in user_tuples:
                ordered_users.append(u[0])
                
                num_pets.append(len(Pet.objects.all().filter(pet_owner = u[0].person)))
                votes = 0 
                for pet in Pet.objects.all().filter(pet_owner = u[0].person):
                    votes = votes + pet.vote_count
                profile_votes.append(votes)
                    
            zipped = zip(ordered_users, num_pets, profile_votes)
            
            
            context['zipped'] = zipped

            
            return render(request, "search_users.html", context=context)

        else:

            context = { 'search' : search_query}


            pets = Pet.objects.all()
            pet_tuples = []
            ordered_pets = []

            def nameMatch(search, p):
                return SequenceMatcher(None, search, p.name).ratio()

            for pet in pets:

                pet_tuples.append((pet, nameMatch(search_query, pet)))

            def takeSecond(elem):
                return elem[1]

            pet_tuples.sort(reverse = True, key=takeSecond)

            for p in pet_tuples:
                ordered_pets.append(p[0])


            context['ordered_pets'] = ordered_pets


            
            return render(request, "search.html", context=context)



    return render(request, "index.html", context=context)





