from django import forms

from django.core.validators import EmailValidator
from django.core.validators import ValidationError
from django.utils.translation import ugettext_lazy as _

# Possible types of carpet
CARPET_TYPE = (
    ('', 'Select a carpet type'),
    ('NRM', 'Normal'),
    ('SLK', 'Silk'),
    ('WOL', 'Wool'),
    ('PER', 'Persian')
)


class CalculationForm(forms.Form):
    carpet_types = forms.ChoiceField(initial='', choices=CARPET_TYPE, label='Carpet Types',)

    length = forms.FloatField(min_value=0)

    width = forms.FloatField(min_value=0)


class ContactForm(forms.Form):
    subject = forms.CharField(label='Subject',
                              required=True)

    email_from = forms.EmailField(label='E-mail address', required=True,
                                  max_length=100,
                                  error_messages={'invalid': 'Please enter a valid email address (e.g. joesmith@abc.com)'},
                                  )  # TODO-me: Change the email address example

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


class PickupForm(forms.Form):  # TODO-me: Used to render the pickup form in the pickup/delivery page
    name = forms.CharField(label='Name', required=True)

    customer_email = forms.EmailField(label='E-mail address', required=True,
                                      max_length=100,
                                      error_messages={'invalid': 'Please enter a valid email address (e.g. joesmith@abc.com)'},
                                      )  # TODO-me: Change the email address example
