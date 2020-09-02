from django import forms
from .models import Organization, Availability

class OrganizationForm(forms.ModelForm):
    class Meta:
        model=Organization
        fields='__all__'
        exclude=['isActive','created','createdBy','lastUpdated','lastUpdatedBy','availability']

class AvailabilityForm(forms.ModelForm):
    class Meta:
        model=Availability
        fields='__all__'
        exclude=['isActive','created','createdBy','lastUpdated','lastUpdatedBy']
