from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate

def check_password(password):
    if len(password)>=8:
        return True
    return False

def check_validation(password):
    has_digit, has_alpha, has_symbols = False, False, False

    for i in password:
        if i.isdigit():
            has_digit =  True
        elif i.isalpha():
            has_alpha = True
        else:
            has_symbols = True
    return has_digit and has_alpha and has_symbols

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
            if not check_password(password) :
                messages.info(request, "Password must be at least 8 symbols")
            elif not check_validation(password):
                messages.info(request,"Password must contain both characters and numbers")
            else:
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

#------------------------------------------------------------------
def changepassword(request):
    if request.user.is_authenticated:
        raise Http404
    if request.method == "POST":
        newpassword1 = request.POST.get("newpassword1")
        newpassword2 = request.POST.get("newpassword2")

        if newpassword1 == newpassword2:
            request.user.set_password(newpassword1)
            request.user.save()
            messages.success(request, "Password changed")

            return redirect("login")
        
    return render(request,'changepassword.html')


