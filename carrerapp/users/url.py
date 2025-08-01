# users/urls.py

from django.urls import path
from .views import add_user_profile

urlpatterns = [
    path('add/', add_user_profile, name='add_user_profile'),
]
