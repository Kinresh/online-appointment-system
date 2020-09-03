from django.urls import path
from . import views

urlpatterns = [
    path('getappointmentdetails/<int:id>', views.getAppointmentDetails, name='getappointmentdetails'),
    
]
