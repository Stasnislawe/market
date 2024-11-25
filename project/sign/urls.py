from django.urls import path
from .views import profile

urlpatterns = [
    path('index', profile, name='profile'),
]