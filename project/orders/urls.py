from django.urls import path

from . import views


urlpatterns = [
    path('create/', views.order_create, name='order_create'),
    path('create/wd', views.order_create2, name='order_create2')
]