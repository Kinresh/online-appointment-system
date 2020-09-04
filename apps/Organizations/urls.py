from django.urls import path
from . import views

urlpatterns = [
    path('', views.viewOrganizations, name='vieworganizations'),
    path('create/', views.createOrganization, name='createorganization'),
    path('<int:id>/update/', views.updateOrganization, name='updateorganization'),
    path('<int:id>/delete/', views.deleteOrganization, name='deleteorganization'),
    path('search/', views.searchOrganization, name='searchorganization'),
    path('search_auto/', views.orgAutoComplete, name='orgautocomplete'),
    path('<int:id>/appointments/', views.viewOrgAppointments, name='vieworgappointments'),
]
