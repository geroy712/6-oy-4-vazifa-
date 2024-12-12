from django.urls import path, include
from .views import index, bmw

urlpatterns = [
    path('', index),
    path('bmw/', bmw),
]