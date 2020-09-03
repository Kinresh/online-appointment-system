from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from django.apps import apps
import apps.Organizations.models
from apps.Organizations.models import Organization, Availability
from apps.Appointments.forms import AppointmentForm
from .forms import UserForm
from apps.Appointments.emails import sendEmail
import threading


def getUserDetails(request, id):
    #id is organizationid
    organization = Organization.objects.get(id=id)
    if request.method == "GET":
        form_user = UserForm()
        form_appointment = AppointmentForm()
    else:
        form_user = UserForm(request.POST)
        form_appointment = AppointmentForm(request.POST)
        if form_user.is_valid() and form_appointment.is_valid():
            try:
                organizationid = request.POST.get('organizationid')
                organization = Organization.objects.get(id=organizationid)
                user = form_user.save()
                f = form_appointment.save(commit=False)
                f.user_id = user.id
                f.organization_id = organizationid
                appointment = f.save()

                t = threading.Thread(target=sendEmail, args=[request, user, organization, appointment])
                t.start()

                return render(request, 'appointment/waitingforconfirmation.html')

            except Exception as exception:
                print("errro in getuserdetails " , exception)
                return HttpResponseRedirect(reverse('searchorganization'))
    context={
        "form_user":form_user,
        "form_appointment":form_appointment,
        "organizationID":id, 
        "organization":organization
        }
    return render(request, 'GetDetails.html',context)

