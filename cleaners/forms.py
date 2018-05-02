from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label='Name',
                           required=True)

    email_from = forms.EmailField(label='E-mail address', required=True,
                                  error_messages={'invalid': 'Your e-mail does not have a valid format.'},
                                  )

    message = forms.CharField(label='Message',
                              required=True)
