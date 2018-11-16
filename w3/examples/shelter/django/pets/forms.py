from django import forms
from pets.models import DOG_AGE_CHOICES, DOG_SIZE_CHOICES, AdoptionApplication


class SearchForm(forms.Form):
    age = forms.ChoiceField(
        label="Age",
        widget=forms.widgets.RadioSelect,
        choices=((None, "Any age"), ) + DOG_AGE_CHOICES,
        required=False)
    size = forms.MultipleChoiceField(
        widget=forms.widgets.CheckboxSelectMultiple,
        label="Size",
        choices=DOG_SIZE_CHOICES,
        required=False)
    good_with_kids = forms.BooleanField(label="Good with kids", required=False)
    good_with_dogs = forms.BooleanField(
        label="Good with other dogs", required=False)
    good_with_cats = forms.BooleanField(label="Good with cats", required=False)


class AdoptionForm(forms.ModelForm):
    class Meta:
        model = AdoptionApplication
        fields = [
            'dog', 'name', 'email', 'current_pet_owner', 'address1',
            'address2', 'city', 'state', 'zip', 'phone_number'
        ]
        widgets = {'dog': forms.HiddenInput()}
