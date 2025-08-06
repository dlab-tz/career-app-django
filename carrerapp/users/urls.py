from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_user_profile, name='add_user_profile'),  # Form is now homepage
]