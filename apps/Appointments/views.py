from django.shortcuts import render
from apps.Organizations.models import Organization, Availability
from apps.Appointments.models import Appointment
from apps.Appointments.forms import AppointmentForm

def getAppointmentDetails(request, id):
    #id is organizationid

    organization = Organization.objects.get(id=id)
    if request.method == "GET":
        form = AppointmentForm()
    else:
        ##form = UserForm(request.POST)
        pass
    context={"form":form,"organizationID":id, "organization":organization}
    return render(request, 'appointment/GetDetails.html',context)
