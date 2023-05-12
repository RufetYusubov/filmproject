from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate

def signup(request):
    if request.method == "POST":
        """
        request.POST = {
        "username" : "rufetyusubov",
        "password" = "rufet123
        }
        
        """
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        if not User.objects.filter(username=username).exists():
            User.objects.create_user(
            username = username,
            password = password
            )
        else :
            messages.info(request,"Username has been taken")
        return redirect("signup")
    return render(request,'signup.html')
#-------------------------------------------------------------

def loginUser(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request,user)
            messages.success(request, "You logged in.")
            return redirect("index")
        else:
            if not User.objects.filter(username=username).exists():
                messages.info(request,"Please enter correct username")
            else:
                messages.info(request,"Please, enter correct password")

    return render(request,'login.html')
#-------------------------------------------------------------------

def logoutUser(request):
    logout(request)
    return redirect("index")


