from . import views
from django.urls import path


urlpatterns = [
    path('', views.home, name = 'scago-home'),
    path('aboutus/', views.aboutus, name = 'scago-aboutus'),
    path('contactus/', views.contactus, name = 'scago-contactus')
]
