from django.urls import path
from . import views

urlpatterns = [
    path('getappointmentdetails/<int:id>', views.getAppointmentDetails, name='getappointmentdetails'),
    path('confirmappointment/<int:id>', views.confirmAppointment, name='confirmappointment'),
    path('completeappointment/<int:id>', views.completeAppointment, name='completeappointment'),
    path('deleteappointment/<int:id>', views.deleteAppointment, name='deleteappointment'),
]
