from django.urls import path
from . import views

urlpatterns = [
    path('getdetails/<int:id>', views.getUserDetails, name='getuserdetails'),
    
]
