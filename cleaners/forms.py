from django import forms

from django.core.validators import EmailValidator
from django.core.validators import ValidationError
from django.utils.translation import ugettext_lazy as _


class ContactForm(forms.Form):
    subject = forms.CharField(label='Subject',
                              required=True)

    email_from = forms.EmailField(label='E-mail address', required=True,
                                  error_messages={'invalid': 'Your e-mail does not have a valid format.'},
                                  )

    message = forms.CharField(label='Message',
                              required=True)

    # Validate email
    def clean_email_from(self):  # TODO-me: Write tests for this
        email = self.cleaned_data['email_from']

        validator = EmailValidator()
        try:
            validator(email)
        except ValidationError:
            raise ValidationError(_('Your email address is invalid. Please enter a correct one'))

        return email
