from django import forms
from django.forms import ModelForm
from .models import Collection
from .fields import YearSelectWidget


class CollectionForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(CollectionForm, self).__init__(*args, **kwargs)
        
        self.fields['post_type'].required = True
        self.fields['title'].required = True
        self.fields['chapter_title'].required = True
        self.fields['publisher_name'].required = True
        self.fields['country_of_publication'].required = True
        self.fields['year_of_publication'].required = True
        self.fields['pages'].required = True
        self.fields['language'].required = True
        self.fields['ISBN'].required = True
        self.fields['DOI'].required = False
        self.fields['link'].required = False
        self.fields['funnding_source'].required = True
        self.fields['guarantor'].required = False

    class Meta:
        model = Collection
        fields = ('post_type', 'title', 'chapter_title', 'publisher_name', 'country_of_publication', 'year_of_publication', 'pages', 'language', 'ISBN', 'DOI', 'link', 'guarantor', 'funnding_source')

        TYPE_CHOICES = [
            ("", ""),
            ("մենագրություն", "մենագրություն"),
            ("կոլեկտիվ մենագրություն", "կոլեկտիվ մենագրություն"),
            ("գիտամեթոդական ձեռնարկ", "գիտամեթոդական ձեռնարկ"),
            ("հոդվածների ժողովածու", "հոդվածների ժողովածու"),
            ("գիտական հրապարակում", "գիտական հրապարակում"),
            ("բառարան", "բառարան"),
            ("հոդված ժողովածույի մեջ", "հոդված ժողովածույի մեջ"),
            ("այլ", "այլ")
        ]

        LANGUAGE_CHOICES = [
            ("", ""),
            ("անգլերեն", "անգլերեն"),
            ("հայերեն", "հայերեն"),
            ("ռուսերեն", "ռուսերեն"),
            ("այլ", "այլ"),
        ]

        widgets = {
            'post_type': forms.Select(choices=TYPE_CHOICES, attrs={'class': 'small-input'}),
            'title': forms.TextInput(attrs={'class': 'small-input'}),
            'chapter_title' : forms.TextInput(attrs={'class': 'small-input'}),
            'publisher_name' : forms.TextInput(attrs={'class': 'small-input'}),
            'country_of_publication' : forms.TextInput(attrs={'class': 'small-input'}),
            'year_of_publication' : YearSelectWidget(attrs={'class': 'small-input'}),
            'pages' : forms.TextInput(attrs={'class': 'small-input'}),
            'language' : forms.Select(choices=LANGUAGE_CHOICES, attrs={'class': 'small-input'}),
            'ISBN' : forms.TextInput(attrs={'class': 'small-input'}),
            'DOI' : forms.TextInput(attrs={'class': 'small-input'}),
            'link' : forms.TextInput(attrs={'class': 'small-input'}),
            'guarantor' : forms.TextInput(attrs={'class': 'small-input'}),
            'funnding_source' : forms.TextInput(attrs={'class': 'small-input'})
        }