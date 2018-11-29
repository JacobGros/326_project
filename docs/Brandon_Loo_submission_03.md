I mainly contributed towards setting up views for displaying a form that allows a logged in user to create a pet submission
and have the data stored to the database.  I achieved this process through creating a class in views.py that uses LoginRequiredMixin for authentication
and CreateView for creating a Model Form of pets that sends the request to the linked html for editable fields as well as initialize fields
like setting the user as the owner of the pet.

In additon, I made changes to the fields in Pets class in models.py to assist with assigning functionalities to specific fields for the html form.
These include assigining choices for the user to pick on pet species as well as give a location to save images uploaded to the form.

Lastly I helped out again with providing advice/bug testing in areas outside of what I was working on, such as suggesting getting rid of pid
as an initialized field in Pets model, as well as which areas the removal would effect and how it can be changed to use pet.id for voting functionality. 
