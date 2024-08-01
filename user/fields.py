from django import forms
from django.forms.widgets import Select
from datetime import datetime
import re
from django.core.exceptions import ValidationError

class YearSelectWidget(Select):
    def __init__(self, attrs=None, years=None):
        now = datetime.now()
        if years is None:
            years = range(now.year, now.year - 100, -1)
        choices = [(year, year) for year in years]
        super().__init__(attrs, choices)

class YearSelectField(forms.TypedChoiceField):
    widget = YearSelectWidget

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('coerce', int)
        super().__init__(*args, **kwargs)

def validate_phone_number(value):
    # Check if the phone number starts with either "+7" or "8" (Russian format)
    if re.match(r'^(\+7|8)[0-9]{10}$', value):
        return

    # Check if the phone number starts with either "+374" or "0" (Armenian format)
    if re.match(r'^(?:\+374|0)[0-9]{8}$', value):
        return

    # If the phone number doesn't match any valid format, raise a validation error
    raise ValidationError('Անվավեր հեռախոսահամարի ձև։ Խնդրում ենք մուտքագրել վավեր ռուսական կամ հայկական հեռախոսահամար։')

def validate_first_letter_uppercase(value):
    if value and not value[0].isupper():
        raise ValidationError("Առաջին տառը մուտքագրել մեծատառ։")
