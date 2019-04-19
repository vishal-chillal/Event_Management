
from django.contrib import admin
from django.conf.urls import include, url

urlpatterns = [
    url(r'', include('event_management.urls')),
    url('admin/', admin.site.urls),
    url('event/', include('event_management.urls'))
]
