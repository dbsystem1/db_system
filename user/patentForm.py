from django import forms
from django.forms import ModelForm
from .models import Patent
from .fields import YearSelectWidget

class PatentForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(PatentForm, self).__init__(*args, **kwargs)
        
        self.fields['authors'].required = True
        self.fields['name'].required = True
        self.fields['registration_country'].required = True
        self.fields['registration_organization'].required = True
        self.fields['patent_number'].required = True
        self.fields['year'].required = False
        self.fields['classification_index'].required = True
        self.fields['authors_count'].required = False
        self.fields['link'].required = False

    class Meta:
        model = Patent
        fields = ('authors', 'name', 'registration_country', 'registration_organization', 'patent_number', 'year', 'classification_index', 'authors_count', 'link')

        widgets = {
            'authors': forms.TextInput(attrs={'class': 'small-input'}),
            'name': forms.TextInput(attrs={'class': 'small-input'}),
            'registration_country' : forms.TextInput(attrs={'class': 'small-input'}),
            'registration_organization' : forms.TextInput(attrs={'class': 'small-input'}),
            'patent_number' : forms.TextInput(attrs={'class': 'small-input'}),
            'year' : YearSelectWidget(attrs={'class': 'small-input'}),
            'classification_index' : forms.TextInput(attrs={'class': 'small-input'}),
            'authors_count' : forms.TextInput(attrs={'class': 'small-input'}),
            'link' : forms.TextInput(attrs={'class': 'small-input'})
        }