from django.urls import path
from . import views

urlpatterns = [
    path('', views.save_profile, name='save_profile'),
    path('verify/<uidb64>/<token>/', views.verify_email, name='verify_email'),
]
