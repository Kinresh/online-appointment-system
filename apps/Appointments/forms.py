from django import forms
from .models import Appointment
from django.contrib.admin.widgets import AdminDateWidget

class AppointmentForm(forms.ModelForm):
    class Meta:
        model=Appointment
        fields='__all__'
        exclude=['isActive','created','createdBy','lastUpdated','lastUpdatedBy','user','organization','status']
        widgets={
            'dateOfAppointment': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control', 'type':'date'}),
            'timeOfAppointment': forms.TimeInput(attrs={'class':'form-control', 'type':'time'}),
        }
        labels={
            'dateOfAppointment': 'Select Date',
            'timeOfAppointment': 'Select Time',
            'reasonOfAppointment': 'Reason (optional)',
        }
