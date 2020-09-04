from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from apps.Organizations.models import Organization, Availability
from apps.Appointments.models import Appointment
from apps.Appointments.forms import AppointmentForm
from .emails import SendAsyncEmail

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

def confirmAppointment(request, id):
    appointment = Appointment.objects.get(isActive=True, id=id)
    appointment.status_id = 2
    appointment.save()
    SendAsyncEmail(request, 2, appointment.user_id, appointment.organization_id, appointment.id)
    return HttpResponseRedirect(reverse('vieworgappointments', kwargs={'id': appointment.organization_id}))

def completeAppointment(request, id):
    appointment = Appointment.objects.get(isActive=True, id=id)
    appointment.status_id = 3
    appointment.save()
    SendAsyncEmail(request, 3, appointment.user_id, appointment.organization_id, appointment.id)
    return HttpResponseRedirect(reverse('vieworgappointments', kwargs={'id': appointment.organization_id}))

def deleteAppointment(request, id):
    appointment = Appointment.objects.get(isActive=True, id=id)
    appointment.isActive = False
    appointment.save()
    return HttpResponseRedirect(reverse('vieworgappointments', kwargs={'id': appointment.organization_id}))