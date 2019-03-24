from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'db', views.dashboard, name='dashboard'),
    url(r'events', views.event, name='events')
]
