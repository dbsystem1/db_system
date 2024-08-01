from django import forms
from django.forms import ModelForm
from .models import Education
from .fields import YearSelectWidget

class EducationForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(EducationForm, self).__init__(*args, **kwargs)
        
        self.fields['university'].required = True
        self.fields['place'].required = True
        self.fields['faculty'].required = True
        self.fields['degree'].required = True
        self.fields['educ_start_year'].required = True
        self.fields['educ_end_year'].required = True
        
    class Meta:
        model = Education
        fields = ('university', 'place', 'faculty', 'degree', 'educ_start_year', 'educ_end_year')

        DEGREE_CHOICES = [
            ("", ""),
            ("բարձրագույն մասնագիտական", "բարձրագույն մասնագիտական"),
            ("բակալավրիատ", "բակալավրիատ"),
            ("մագիստրատուրա", "մագիստրատուրա"),
            ("ասպիրանտուրա", "ասպիրանտուրա"),
            ("դոկտորատուրա", "դոկտորատուրա"),
        ]

        widgets = {
            'university': forms.TextInput(attrs={'class': 'small-input'}),
            'place' : forms.TextInput(attrs={'class': 'small-input'}),
            'faculty' : forms.TextInput(attrs={'class': 'small-input'}),
            'degree' : forms.Select(choices=DEGREE_CHOICES, attrs={'class': 'small-input'}),
            'educ_start_year' : YearSelectWidget(attrs={'class': 'small-input'}),
            'educ_end_year' : YearSelectWidget(attrs={'class': 'small-input'}),
        }