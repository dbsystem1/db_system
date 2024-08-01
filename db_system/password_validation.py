# app_name/password_validation.py
from django import forms
from re import compile as recompile
import re
from django.utils.translation import gettext as _
from django.core.exceptions import ValidationError

class PinValidator:
    def validate(self, password, user=None):
        # Your custom password validation logic here
        if len(password) < 6:
            raise ValidationError(_("The password must contain at least 6 characters."))
        if not any(char.isupper() for char in password):
            raise ValidationError(_("The password must contain at least one uppercase letter."))
        if not any(char.islower() for char in password):
            raise ValidationError(_("The password must contain at least one lowercase letter."))
        if not any(char in '!@#$%^&*(),.?":{}|<>' for char in password):
            raise ValidationError(_("The password must contain at least one special symbol."))

    def get_help_text(self):
        return _("Your password must contain at least one uppercase letter, one lowercase letter, and one special symbol.")
    