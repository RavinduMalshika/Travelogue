from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('destinations', views.DestinationView.as_view(), name='destination-list')
]