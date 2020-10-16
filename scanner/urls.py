from django.urls import path, include
from . import views

urlpatterns = [
    path('scanner/', views.scanner, name='scanner-scan')
]
