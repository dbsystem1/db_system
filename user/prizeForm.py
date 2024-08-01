from django import forms
from django.forms import ModelForm
from .models import Prize
from .fields import YearSelectWidget

class PrizeForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(PrizeForm, self).__init__(*args, **kwargs)
        
        self.fields['name'].required = True
        self.fields['branch'].required = False
        self.fields['type'].required = True
        self.fields['giver'].required = True
        self.fields['reason'].required = False
        self.fields['year'].required = True
        self.fields['link'].required = True

    class Meta:
        model = Prize
        fields = ('name', 'branch', 'type', 'giver', 'reason', 'year', 'link')

        TYPE_CHOICES = [
            ("", ""),
            ("անհատական", "անհատական"),
            ("խմբային", "խմբային"),
        ]

        widgets = {
            'name': forms.TextInput(attrs={'class': 'small-input'}),
            'branch': forms.TextInput(attrs={'class': 'small-input'}),
            'type' : forms.Select(choices=TYPE_CHOICES, attrs={'class': 'small-input'}),
            'giver' : forms.TextInput(attrs={'class': 'small-input'}),
            'reason' : forms.TextInput(attrs={'class': 'small-input'}),
            'year' : YearSelectWidget(attrs={'class': 'small-input'}),
            'link' : forms.TextInput(attrs={'class': 'small-input'})
        }