
from django.urls import path

from . import views

urlpatterns = [
    path('', views.enpoints, name='endpoints'),
    path('overview', views.overview, name='overview'),
    path('product/<str:pk>/', views.product_detail, name='product_detail'),
]