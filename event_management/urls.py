from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.SignupPageView.as_view(), name='register'),
    url(r'^signup', views.SignupPageView.as_view(), name='register'),
    url(r'^signin', views.SigninPageView.as_view(), name='login'),
    url(r'^register_user', views.register, name='register_user'),
    url(r'^login_user', views.login_user, name='login_user')
    # url(r'^events', views.register, name='signup_user')
]
