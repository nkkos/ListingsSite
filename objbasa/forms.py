from django import forms
from .models import Listing
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class NListing(forms.ModelForm):

    class Meta:
        model = Listing
        fields = ('title', 'address','show_address', 'price', 'space_type',)

class NewUser(UserCreationForm):

    class Mets:
        model = User
        fields = ('username', "password1", 'password2')
