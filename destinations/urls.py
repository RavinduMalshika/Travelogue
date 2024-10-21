from django.urls import path
from . import views

urlpatterns = [
    path('destinations', views.DestinationView.as_view(), name='destination-list'),
    path('destinations/create', views.create, name='create-destination'),
]