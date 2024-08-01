from django import forms
from django.forms import ModelForm
from .models import Dissertation
from django.forms import SelectDateWidget
from .fields import YearSelectWidget

class DissertationForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(DissertationForm, self).__init__(*args, **kwargs)
        
        self.fields['title'].required = True
        self.fields['code'].required = True
        self.fields['organization'].required = False
        self.fields['protection_year'].required = True
        self.fields['confirmation_date'].required = False
        self.fields['name'].required = False
        self.fields['password'].required = True

    class Meta:
        model = Dissertation
        fields = ('title', 'code', 'organization', 'protection_year', 'confirmation_date', 'name', 'password')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'small-input'}),
            'code': forms.TextInput(attrs={'class': 'small-input'}),
            'organization' : forms.TextInput(attrs={'class': 'small-input'}),
            'protection_year' : YearSelectWidget(attrs={'class': 'small-input'}),
            'confirmation_date' : SelectDateWidget(years=range(1900, 2025), attrs={'class': 'small-input'}),
            'name' : forms.TextInput(attrs={'class': 'small-input'}),
            'password': forms.TextInput(attrs={'class': 'small-input'})
        }
