from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.redirect_view, name='base'),

    url(r'^signup', views.SignupPageView.as_view(), name='register'),
    url(r'^signin', views.SigninPageView.as_view(), name='login'),
    url(r'^dashboard', views.DashboardPageView.as_view(), name='dashboard'),

    url(r'register_user', views.register_user, name='register_user'),
    url(r'login_user', views.login_user, name='login_user'),
    url(r'^add_event', views.events, name="add_event")
]
