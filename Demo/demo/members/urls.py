from django.urls import path
from . import views


urlpatterns = [
    path('login_user', views.login_user, name="userin"),
    path('logout_user', views.logout_user, name='signout'),
    path('register_user', views.register_user, name='register_user'),
]
