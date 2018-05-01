from django import forms


class ContactForm(forms.Form):
    name = forms.CharField
    email_from = forms.EmailField(required=True,
                                  error_messages={'invalid': 'Your e-mail does not have a valid format.'},
                                  )

