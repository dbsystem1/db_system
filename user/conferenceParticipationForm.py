from django import forms
from django.forms import ModelForm
from .models import Conference
from django.forms import SelectDateWidget

class ConferenceParticipationForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ConferenceParticipationForm, self).__init__(*args, **kwargs)
        
        self.fields['name'].required = True
        self.fields['country'].required = True
        self.fields['date'].required = True
        self.fields['authors'].required = True
        self.fields['authors_count'].required = True

    class Meta:
        model = Conference
        fields = ('name', 'country', 'date', 'authors', 'authors_count')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'small-input'}),
            'country' : forms.TextInput(attrs={'class': 'small-input'}),
            'date' : SelectDateWidget(years=range(1900, 2025), attrs={'class': 'small-input'}),
            'authors' : forms.TextInput(attrs={'class': 'small-input'}),
            'authors_count' : forms.TextInput(attrs={'class': 'small-input'})
        }