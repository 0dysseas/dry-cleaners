from django import forms

from django.core.validators import EmailValidator
from django.core.validators import ValidationError
from django.utils.translation import ugettext_lazy as _


class ContactForm(forms.Form):
    name = forms.CharField(label='Name',
                           required=True)

    email_from = forms.EmailField(label='E-mail address', required=True,
                                  error_messages={'invalid': 'Your e-mail does not have a valid format.'},
                                  )

    message = forms.CharField(label='Message',
                              required=True)

    # Validate email
    def clean_email_from(self):
        email = self.cleaned_data['email_from']

        validator = EmailValidator()
        try:
            validator(email)
        except Exception:
            raise ValidationError(_('Invalid e-mail address'),
                                  code='invalid')
