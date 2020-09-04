from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
import json
from .forms import OrganizationForm, AvailabilityForm
from .models import Organization, Availability
from apps.Appointments.models import Appointment
from apps.Users.models import User

def createOrganization(request):
    if request.method == "GET":
        form = OrganizationForm()
        form_availability= AvailabilityForm()
    else:
        form = OrganizationForm(request.POST, request.FILES)
        form_availability= AvailabilityForm(request.POST)
        if form.is_valid() and form_availability.is_valid():
            try:
                faobj=form_availability.save()
                f = form.save(commit=False)
                f.availability_id = faobj.id
                f.createdBy = request.user.id
                f.save()
                return HttpResponseRedirect(reverse('vieworganizations'))
            except:
                print('Errror in createOrganization method')
    context={"form":form,"form_availability":form_availability}
    return render(request,'organization/CreateOrganization.html',context)

def viewOrganizations(request):
    data = Organization.objects.filter(isActive=True,createdBy=request.user.id)
    context={"data":data}
    return render(request,'organization/ViewOrganizations.html',context)

def updateOrganization(request, id):
    obj = Organization.objects.get(id=id)
    if obj.availability is not None:
        obj_availability = Availability.objects.get(id=obj.availability.id)
    if request.method == "GET":
        form = OrganizationForm(instance=obj)
        form_availability = AvailabilityForm(instance=obj_availability)
    else: 
        form = OrganizationForm(request.POST, request.FILES, instance=obj)
        form_availability = AvailabilityForm(request.POST, instance=obj_availability)
        if form.is_valid():
            try:
                faobj=form_availability.save()
                f=form.save(commit=False)
                f.availability_id = faobj.id
                f.lastUpdatedBy = request.user.id
                f.save()
                return HttpResponseRedirect(reverse('vieworganizations'))
            except:
                print("error in updateOrganization method")
    context={"form":form,"form_availability":form_availability}
    return render(request,'organization/CreateOrganization.html',context)

def deleteOrganization(request, id):
    obj = Organization.objects.get(id=id)
    obj.isActive=False
    obj.save()
    return HttpResponseRedirect(reverse('vieworganizations'))

def searchOrganization(request):
    if request.method == "POST":
        q=request.POST.get('organization')
        orgName=q.split(',')[0]
        data = Organization.objects.filter(name=orgName)
        context={"data":data}
    else: 
        context={}
    return render(request,'organization/SearchOrganization.html',context)

def orgAutoComplete(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        organizations = Organization.objects.filter(name__icontains=q)
        results = []
        for org in organizations:
            org_json = {}
            org_json = org.name + ", " + org.city
            results.append(org_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)

def viewOrgAppointments(request, id):
    appointments = Appointment.objects.filter(isActive=True, organization_id=id)
    context={"appointments":appointments}
    return render(request,'organization/ViewAppointments.html',context)