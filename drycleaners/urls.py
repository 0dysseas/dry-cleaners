from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^dry-cleaners/', include('cleaners.urls')),
    url(r'^admin/', admin.site.urls),
]
