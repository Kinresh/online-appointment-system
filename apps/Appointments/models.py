from django.db import models
from apps.Users.models import User
from apps.Organizations.models import Organization

class Status(models.Model):
    status= models.CharField(max_length=100)
    def __str__(self):
        return self.status

class Appointment(models.Model):
    #userid
    user=models.ForeignKey(User,on_delete=models.DO_NOTHING)
    #organizationid
    organization= models.ForeignKey(Organization,on_delete=models.DO_NOTHING)

    status= models.ForeignKey(Status,on_delete=models.DO_NOTHING, default=1)
    dateOfAppointment= models.DateField()
    timeOfAppointment= models.TimeField()
    reasonOfAppointment= models.CharField(max_length=200,blank=True)
    
    isActive= models.BooleanField(default=True)
    created= models.DateTimeField(auto_now_add=True)
    createdBy= models.CharField(max_length=200, blank=True)
    lastUpdated= models.DateTimeField(auto_now=True)
    lastUpdatedBy= models.CharField(max_length=200, blank=True)
