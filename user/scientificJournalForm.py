from django import forms
from django.forms import ModelForm
from .models import Article
from django.forms import SelectDateWidget
from .fields import YearSelectWidget

class ArticleForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ArticleForm, self).__init__(*args, **kwargs)
        
        self.fields['publication_repository'].required = True
        self.fields['DOI'].required = True
        self.fields['ISSN_print'].required = True
        self.fields['ISSN_electronic'].required = True
        self.fields['title'].required = True
        self.fields['magazine_name'].required = True
        self.fields['year'].required = True
        self.fields['pages_count'].required = True
        self.fields['language'].required = True
        self.fields['link'].required = True
        self.fields['funding_source'].required = True
        self.fields['volume'].required = True

    class Meta:
        model = Article
        fields = ('publication_repository', 'DOI', 'ISSN_print', 'ISSN_electronic', 'title', 'magazine_name', 'year', 'pages_count', 'language', 'link', 'funding_source', 'volume', 'quartile')

        REPOSITORY_CHOICES = [
            ("", ""),
            ("WOS-ԱԳ (IF) ունեցող պարբերական", "WOS-ԱԳ (IF) ունեցող պարբերական"),
            ("Scopus", "Scopus"),
            ("ՀՀ ԲՈԿ ցանկ", "ՀՀ ԲՈԿ ցանկ"),
            ("ՌԴ ԲՈԿ ցանկ", "ՌԴ ԲՈԿ ցանկ"),
            ("այլ", "այլ")
        ]

        LANGUAGE_CHOICES = [
            ("", ""),
            ("անգլերեն", "անգլերեն"),
            ("հայերեն", "հայերեն"),
            ("ռուսերեն", "ռուսերեն"),
            ("այլ", "այլ"),
        ]

        QUARTILE_CHOICES = [
            ("", ""),
            ("Q1", "Q1"),
            ("Q2", "Q2"),
            ("Q3", "Q3"),
            ("Q4", "Q4"),
        ]

        widgets = {
            'publication_repository': forms.Select(choices=REPOSITORY_CHOICES, attrs={'class': 'small-input'}),
            'DOI' : forms.TextInput(attrs={'class': 'small-input'}),
            'ISSN_print' : forms.TextInput(attrs={'class': 'small-input'}),
            'ISSN_electronic' : forms.TextInput(attrs={'class': 'small-input'}),
            'title' : forms.TextInput(attrs={'class': 'small-input'}),
            'magazine_name' : forms.TextInput(attrs={'class': 'small-input'}),
            'year' : YearSelectWidget(attrs={'class': 'small-input'}),
            'pages_count' : forms.TextInput(attrs={'class': 'small-input'}),
            'language' : forms.Select(choices=LANGUAGE_CHOICES, attrs={'class': 'small-input'}),
            'link' : forms.TextInput(attrs={'class': 'small-input'}),
            'funding_source' : forms.TextInput(attrs={'class': 'small-input'}),
            'volume' : forms.TextInput(attrs={'class': 'small-input'}),
            'quartile': forms.Select(choices=QUARTILE_CHOICES, attrs={'class': 'small-input'}),
        }