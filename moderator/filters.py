import django_filters

from django import forms
from user.models import *


class ProfessorDegreeFilterForm(forms.Form):
    professor_first_name = forms.CharField(required=False)
    professor_last_name = forms.CharField(required=False)
    professor_patronomic = forms.CharField(required=False)
    professor_gender = forms.CharField(required=False)
    professor_membership_of_RA_NAS = forms.CharField(required=False)
    professor_position = forms.CharField(required=False)
    professor_domain = forms.CharField(required=False)
    professor_smaller_age = forms.IntegerField(required=False)
    professor_bigger_age = forms.IntegerField(required=False)
    professor_work_time = forms.CharField(required=False)
    degree_science = forms.CharField(required=False)
    degree_degree = forms.CharField(required=False)
    