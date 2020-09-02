from django.db import models
from datetime import datetime

default_id= 1

class Availability(models.Model):

    monday_from= models.TimeField(blank=True, default='20:00')
    monday_to= models.TimeField(blank=True, default='20:00')
    tueday_from= models.TimeField(blank=True, default='20:00')
    tueday_to= models.TimeField(blank=True, default='20:00')
    wednesday_from= models.TimeField(blank=True, default='20:00')
    wednesday_to= models.TimeField(blank=True, default='20:00')
    thursday_from= models.TimeField(blank=True, default='20:00')
    thursday_to= models.TimeField(blank=True, default='20:00')
    friday_from= models.TimeField(blank=True, default='20:00')
    friday_to= models.TimeField(blank=True, default='20:00')
    saturday_from= models.TimeField(blank=True, default='20:00')
    saturday_to= models.TimeField(blank=True, default='20:00')
    sunday_from= models.TimeField(blank=True, default='20:00')
    sunday_to= models.TimeField(blank=True, default='20:00')

    isActive= models.BooleanField(default=True)
    createdBy= models.CharField(max_length=200, blank=True)
    created= models.DateTimeField(auto_now_add=True, null=True)
    lastUpdatedBy= models.CharField(max_length=200, blank=True)
    lastUpdated= models.DateTimeField(auto_now=True, null=True)

class Org_Type(models.Model):
    organizationType= models.CharField(max_length=100)
    def __str__(self):
        return self.organizationType

class Organization(models.Model):
    name= models.CharField(max_length=50, unique=True)
    #password= models.CharField(max_length=100, blank=True)    
    organizationType= models.ForeignKey(Org_Type, on_delete=models.DO_NOTHING)
    availability= models.ForeignKey(Availability, on_delete=models.CASCADE, default=default_id) 
    address= models.CharField(max_length=200)
    city= models.CharField(max_length=100)
    state= models.CharField(max_length=100)
    country= models.CharField(max_length=100)
    zipcode= models.CharField(max_length=20)
    phno1= models.CharField(max_length=10, unique=True)
    phno2= models.CharField(max_length=10, unique=True, blank=True)
    phno3= models.CharField(max_length=10, unique=True, blank=True)
    emailAddress= models.EmailField(max_length=100, blank=True)
    photo1= models.ImageField(upload_to='photos/organization/', blank=True)
    photo2= models.ImageField(upload_to='photos/organization/', blank=True)
    photo3= models.ImageField(upload_to='photos/organization/', blank=True)
    photo4= models.ImageField(upload_to='photos/organization/', blank=True)
    photo5= models.ImageField(upload_to='photos/organization/', blank=True)
    websiteLink= models.CharField(max_length=100, blank=True)
    description= models.TextField(blank=True)
    #comma separeted
    #services= models.CharField(max_length=200, blank=True)
    #isVerified= models.BooleanField(default=False)
    #liveField= models.TextField(blank=True)
    #directConfirm= models.BooleanField(default=False)
    
    

    isActive= models.BooleanField(default=True)
    created= models.DateTimeField(auto_now_add=True)
    createdBy= models.CharField(max_length=200, blank=True)
    lastUpdated= models.DateTimeField(auto_now=True)
    lastUpdatedBy= models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name

