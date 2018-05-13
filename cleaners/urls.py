from django.conf.urls import url
from . import views

# Namespace to differentiate among apps
app_name = 'cleaners'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about$', views.about, name='about'),
    url(r'^services$', views.services, name='services'),
    url(r'^pick-up$', views.pick_up, name='pick_up'),
    url(r'^contact$', views.contact, name='contact'),
    url(r'^thank-you', views.thank_you, name='thank_you'),
    url(r'^one_page$', views.one_page, name='one_page'),  # TODO-me: To be removed?
]
