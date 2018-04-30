from django.conf.urls import url
from . import views

app_name = 'cleaners'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about$', views.about, name='about'),
    url(r'^one_page$', views.one_page, name='one_page'),
]