from django.urls import path, include 
from . import views


# localhost:8000/chai
# localhost:8000/chai/order
urlpatterns = [
    path('', views.all_chai, name = 'all_chai'),

]
