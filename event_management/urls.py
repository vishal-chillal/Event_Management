from django.conf.urls import url
from . import views

# urlpatterns = [
#     url(r'^$', views.index, name='index'),
#     url(r'db', views.dashboard, name='dashboard'),
#     url(r'events', views.event, name='events')
# ]

urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name='home'), # Notice the URL has been named
    url(r'^about/$', views.AboutPageView.as_view(), name='about'),
]