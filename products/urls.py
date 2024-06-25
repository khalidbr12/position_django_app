from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_search, name='product_search'),
    path('print/', views.print_products, name='print_products'),
    path('clear/', views.clear_selection, name='clear_selection'),
]