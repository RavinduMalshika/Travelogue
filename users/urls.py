from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('user', views.UserProfileView.as_view(), name='user'),
    path('logout', views.logout, name='logout'),
]