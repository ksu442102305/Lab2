from django.urls import path
from . import views

urlpatterns = [
    path('', views.default, name='default'),
    path('<str:number>/', views.calculate_tax, name='calculate_tax'),
    path('taxrate/', views.tax_rate, name='tax_rate'),
]
