from django import forms
from Find_Homes.models import Listing, Location


class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = '__all__'


class ListingForm(forms.ModelForm):

    class Meta:
        model = Listing
        exclude = ['location']



# class EditListing(forms.ModelForm):
#     class Meta:
#         model = Listing
#         exclude = ['location']
