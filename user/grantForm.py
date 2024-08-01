from django import forms
from django.forms import ModelForm
from .models import Grant
from .fields import YearSelectWidget

class GrantForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(GrantForm, self).__init__(*args, **kwargs)
        
        self.fields['type'].required = False
        self.fields['status'].required = False
        self.fields['title'].required = True
        self.fields['grant_code'].required = True
        self.fields['start'].required = False
        self.fields['duration_months'].required = False
        self.fields['financial_volume'].required = True
        self.fields['link'].required = False
        self.fields['publication_num'].required = False

    class Meta:
        model = Grant
        fields = ('type', 'status', 'title', 'grant_code', 'grantor', 'start', 'duration_months', 'financial_volume', 'link', 'publication_num')

        TYPE_CHOICES = [
            ("", ""),
            ("պայմանագրային (թեմատիկ) ֆինանսավորման թեմա", "պայմանագրային (թեմատիկ) ֆինանսավորման թեմա"),
            ("դրամաշնորհ", "դրամաշնորհ"),
        ]

        STATUS_CHOICES = [
            ("", ""),
            ("ղեկավար", "ղեկավար"),
            ("համաղեկավար", "համաղեկավար"),
            ("խմբի անդամ", "խմբի անդամ"),
        ]

        widgets = {
            'type': forms.Select(choices=TYPE_CHOICES, attrs={'class': 'small-input'}),
            'status': forms.Select(choices=STATUS_CHOICES, attrs={'class': 'small-input'}),
            'title' : forms.TextInput(attrs={'class': 'small-input'}),
            'grant_code' : forms.TextInput(attrs={'class': 'small-input'}),
            'grantor' : forms.TextInput(attrs={'class': 'small-input'}),
            'start' : YearSelectWidget(attrs={'class': 'small-input'}),
            'duration_months' : forms.TextInput(attrs={'class': 'small-input'}),
            'financial_volume' : forms.TextInput(attrs={'class': 'small-input'}),
            'link' : forms.TextInput(attrs={'class': 'small-input'}),
            'publication_num' : forms.TextInput(attrs={'class': 'small-input'})
        }