from django.urls import path
from . import views


urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('category/<slug:cat_slug>',
        views.categories_list,
        name='product_list_by_category'),
    path('product/<slug:prd_slug>',
        views.product_detail,
        name='product_detail'),
]