from django.shortcuts import render
from .forms import UserForm

def getUserDetails(request, id):
    if request.method == "GET":
        form = UserForm()
    else:
        pass    
    context={"form":form,"organizationID":id}
    return render(request, 'user/GetDetails.html',context)
