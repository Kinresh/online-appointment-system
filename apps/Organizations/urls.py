from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.createOrganization, name='createorganization'),
    path('', views.viewOrganizations, name='vieworganizations'),
    path('update/<int:id>/', views.updateOrganization, name='updateorganization'),
    path('delete/<int:id>/', views.deleteOrganization, name='deleteorganization'),
    path('search/', views.searchOrganization, name='searchorganization'),
    path('search_auto/', views.orgAutoComplete, name='orgautocomplete'),
    path('<int:id>/appointments/', views.viewOrgAppointments, name='vieworgappointments'),
]
