from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.


def profile(request):
    return render(request, 'sign/profile.html')