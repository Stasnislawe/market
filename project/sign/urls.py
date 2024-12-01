from django.urls import path
from .views import ProfileView

urlpatterns = [
    path('index', ProfileView.as_view(), name='profile'),
]