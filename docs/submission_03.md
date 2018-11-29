Overview: New changes include the user interaction with website forms such as submitting pets to the database, voting for pets. Some
removing of the superfluous aspects of the models. The images of pets are now linked with the correct species. Also changes to init.py 
and the ability to create new users. Also changes to the template pages to fully-account for all the necessary data, functioning form 
-buttons, new images with alt-text, formatting, reset button to reset the form, and more. Added a display of the pets owned by a person to their user-page and their total pet-votes. Changes to the layout of pages on the website, and form design for the pages also. Authentication support and log-in requirements were also added for the website and for the ability to use the functions on the forms.

Team Members: Joseph Capozzi, Brandon Loo, Jacob Grosner, Patrick Robb

Video Link:

Design Overview: Users can access the home screen and leaderboard screen without logging in. Once logged in, they can vote for pets, view their profile (and their pets), and submit pets. An important view change is on the voting screen, a user cannot see their own pet, and clicking on 'my profile' will return a a detailed view on the user that clicks it. Their is also lots of form interaction/adusting database models within the project. Simplest one, users can vote for pets, incrementing that pet model's vote count. More impressively, users who don't have an account can register for one, adding a user and person (person extends user)to the database. Another critical feature is that users, once logged in, can upload their pets, adding a brand new pet model to the database, allowing other users to vote for it. 

Problems/Successes: 
Problems:
There were some problems getting user-submitted pets to save to the database through the form submission.
Some members had computer problems.
I (Jacob) didn't do anything over break, resulting in some quick code crunching on Sunday and Monday.
Content in general required outside sources to consult to fully grasp.

Successes:
App functionaliy is pretty much done(Every goal has been met, adding extra stuff (nice css, extra stats) is the new goal).
Our team choice is also already done(we've been working with images since October).
Images of pets are now associated with the appropriate species.
Users and person class are now linked, fufilling all our hopes and dreams.
Coding work was more evenly distrubuted out amongst members this time, a definite improvement from project 02. 

Team Choice: Our team choice is all about images. We had to research outside of class to figure out how we could allow users to upload images, have the images be saved to the database, and then be displayed to other users. We also had to taylor init.py to assign images to our models. 
