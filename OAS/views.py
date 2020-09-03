from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

@login_required(login_url='loginpage')
def home(request):
    return render(request,'index.html')

def register(request):
    if request.method == "GET":
        form = UserCreationForm()
    else:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return HttpResponseRedirect(reverse('loginpage'))
            except:
                print("error in register method")
                return HttpResponseRedirect(reverse('registerpage'))
    context={"form":form}
    return render(request,'user/register.html',context)


def loginpage(request):
    if request.method == "GET":
        pass
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('homepage'))
        else:
            print("incorrect username or password")
            return HttpResponseRedirect(reverse('loginpage'))
    context={}
    return render(request,'user/login.html',context)

def logoutpage(request):
    logout(request)
    return HttpResponseRedirect(reverse('loginpage'))