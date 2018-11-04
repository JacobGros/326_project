from django import forms


picture  = forms.ImageField(label = 'Upload your cute pet pics!',
                                          help_text = 'The image should be cute.')
