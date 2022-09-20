from django.urls import path
from .views import UserRegisterVeiw

urlpatterns = [
    path('register/', UserRegisterVeiw.as_view(), name='register'),
]