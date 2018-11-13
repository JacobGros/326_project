I contributed to several aspects of this project. For starters, I worked with Patrick on the models.py, getting them set up.
Then I fixed an issue we had with naming one of our models, User, which Django already has a class for. I did this by making a
new model named Person, and getting rid of all traces of our own User class(except for it's definition in models.py, Django didn't
like me altering that one). I also applied some edits to the models.py: We originally didn't have pet_owner as a foreign key for pet,
which I made. We also had a pet id field for person, which doesn't make any sense, because a person doesn't need to have a pet.

In addition, I wrote both the init2.py script and the init.sh script to run it.(Init.py was the first population script we had,
but it was full of errors, and after two hours of debugging, we gave up and I wrote the entire script myself). The problem I solved
when writing init2.py was the issue of saving and displaying an image in Django. No one in my group knew how to do it,
so when I had to upload an image for each pet, I wound up solving that problem and editing the models.py to 
properly store images for pets. 

Lastly, I also worked on views.py to calculate the ranking of pets based off of cuteness, the cutest pet, etc. and was able
to pass that data to the templates, where I displayed it. Specfically I wrote the complete templates for 
the vote page and the leaderboard page. While I edited the homepage(index)template to include a display of the cutest pet, as
determined by the number of votes. 

Smaller contributons include editing data model diagrams and helping the team with Git and command line stuff. 

For exactly what I contributed on the code front, please see repository commits. 
(Also worth noting that any commit by author Vagrant is Patrick's commit and not mine)
