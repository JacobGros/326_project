from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from PUPG.models import Person

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    country = forms.CharField(max_length=30, required=False, help_text='Optional.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'country', 'password1', 'password2', )

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name',)

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('country', 'name')

#picture  = forms.ImageField(label = 'Upload your cute pet pics!',
 #                                         help_text = 'The image should be cute.')
