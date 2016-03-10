from django import forms
from .models import Listing

class NListing(forms.ModelForm):

    class Meta:
        model = Listing
        fields = ('title', 'address','show_address', 'price', 'space_type',)
