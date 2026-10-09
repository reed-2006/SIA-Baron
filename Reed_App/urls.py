from django.urls import path
from . import views

urlpatterns = [
    path('pet_management/', views.pet, name='pet'),
]
