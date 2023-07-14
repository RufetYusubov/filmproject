from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from film.models import Category
from django.views.generic import View

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

# def capital_letter(password):
#     capital_letter = ""
#     for i in password:
#         if i.isalpha():
#             capital_letter+=i
#     a = 0
#     for i in capital_letter:
#         if i.isupper():
#             a+=1
#     if a>0 and a<2:
#         return True
#     return False

class SignupView(View):
    def get(self,request,*args,**kwargs):
        categories = Category.objects.all()
        context = {
            "categories" : categories
        }
        return render(request,'signup.html', context)
    
    def post(self,request,*args,**kwargs):
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        if not User.objects.filter(username=username).exists():
            if not check_password(password) :
                messages.info(request, "Password must be at least 8 symbols")
                return redirect('signup')
            elif not check_validation(password):
                messages.info(request,"Password must contain both characters and numbers")
                return redirect('signup')
            else:
                User.objects.create_user(
                username = username,
                password = password
            )
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "You logged in.")
                return redirect("index")
        else:
            messages.info(request,"Username has been taken")
            return redirect("signup")



# def signup(request):
#     categories = Category.objects.all()
#     context = {
#         "categories" : categories
#     }

#     if request.method == "POST":
#         """
#         request.POST = {
#         "username" : "rufetyusubov",
#         "password" = "rufet123
#         }
        
#         """
#         username = request.POST.get("username")
#         password = request.POST.get("password")
        
#         if not User.objects.filter(username=username).exists():
#             if not check_password(password) :
#                 messages.info(request, "Password must be at least 8 symbols")
#                 return redirect('signup')
#             elif not check_validation(password):
#                 messages.info(request,"Password must contain both characters and numbers")
#                 return redirect('signup')
#             else:
#                 User.objects.create_user(
#                 username = username,
#                 password = password
#             )
#             user = authenticate(request, username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 messages.success(request, "You logged in.")
#                 return redirect("index")
#         else:
#             messages.info(request,"Username has been taken")
#             return redirect("signup")
#     return render(request,'signup.html', context)
#-------------------------------------------------------------
class LoginUserView(View):
    def get(self,request,*args,**kwargs):
        categories = Category.objects.all()
        context = {
            "categories" : categories
        }
        return render(request,'login.html', context)
    
    def post(self,request,*args,**kwargs):
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
            return redirect("login")
            
            
        



# def loginUser(request):
#     categories = Category.objects.all()
#     context = {
#         "categories" : categories
#     }
#     if request.method == "POST":
#         username = request.POST.get("username")
#         password = request.POST.get("password")

#         user = authenticate(request, username=username, password=password)

#         if user is not None:
#             login(request,user)
#             messages.success(request, "You logged in.")
#             return redirect("index")
#         else:
#             if not User.objects.filter(username=username).exists():
#                 messages.info(request,"Please enter correct username")
#             else:
#                 messages.info(request,"Please, enter correct password")

#     return render(request,'login.html', context)
#-------------------------------------------------------------------

def logoutUser(request):
    logout(request)
    return redirect("index")

#------------------------------------------------------------------
class ChangepasswordView(View):
    def get(self,request,*args,**kwargs):
        categories = Category.objects.all()
        context = {
            "categories" : categories
        }
        return render(request,'changepassword.html', context)
    
    def post(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            raise Http404
        username = request.POST.get("username")
        newpassword1 = request.POST.get("newpassword1")
        newpassword2 = request.POST.get("newpassword2")
        user = User.objects.get(username=username)

        if newpassword1 == newpassword2:
            user.set_password(newpassword1)
            user.save()
            messages.success(request, "Password changed")

        return redirect("login")


# def changepassword(request):
#     categories = Category.objects.all()
#     context = {
#         "categories" : categories
#     }
#     if request.user.is_authenticated:
#         raise Http404
#     if request.method == "POST":
#         username = request.POST.get("username")
#         newpassword1 = request.POST.get("newpassword1")
#         newpassword2 = request.POST.get("newpassword2")
#         user = User.objects.get(username=username)

#         # print(username, newpassword1, newpassword2, user)

#         if newpassword1 == newpassword2:
#             user.set_password(newpassword1)
#             user.save()
#             messages.success(request, "Password changed")

#         return redirect("login")
        
#     return render(request,'changepassword.html', context)
#-------------------------------------------------------------------------
class SettingsView(View):
    def get(self,request,*args,**kwargs):
        categories = Category.objects.all()
        context = {
            "categories" : categories
        }
        return render(request, 'settings.html', context)
    def post(self,request,*args,**kwargs):
        if not request.user.is_authenticated:
            raise Http404
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        username = request.POST.get("username")
        oldpassword = request.POST.get("oldpassword")
        newpassword = request.POST.get("newpassword")
        if firstname:
            request.user.first_name = firstname
            request.user.save()
        if lastname:
            request.user.last_name = lastname
            request.user.save()
        if username:
            request.user.username = username
            request.user.save()
        if oldpassword and newpassword:
            if request.user.check_password(oldpassword):
                if not check_password(newpassword):
                    messages.info(request,"Password must be at least 8 symbols")
                elif not check_validation(newpassword):
                    messages.info(request, "Password must contain both characters and numbers")
                else:
                    request.user.set_password(newpassword)
                    request.user.save()
            else:
                messages.info(request, "Please enter correct oldpassword")
                return redirect("settings")
            return redirect("settings")
            



# def settings(request):
#     categories = Category.objects.all()
#     context = {
#         "categories" : categories
#     }
#     if not request.user.is_authenticated:
#         raise Http404
#     if request.method == "POST":
#         firstname = request.POST.get("firstname")
#         lastname = request.POST.get("lastname")
#         username = request.POST.get("username")
#         oldpassword = request.POST.get("oldpassword")
#         newpassword = request.POST.get("newpassword")
#         if firstname:
#             request.user.first_name = firstname
#             request.user.save()
#         if lastname:
#             request.user.last_name = lastname
#             request.user.save()
#         if username:
#             request.user.username = username
#             request.user.save()
#         if oldpassword and newpassword:
#             if request.user.check_password(oldpassword):
#                 if not check_password(newpassword):
#                     messages.info(request,"Password must be at least 8 symbols")
#                 elif not check_validation(newpassword):
#                     messages.info(request, "Password must contain both characters and numbers")
#                 else:
#                     request.user.set_password(newpassword)
#                     request.user.save()
#             else:
#                 messages.info(request, "Please enter correct oldpassword")
            
#     return render(request, 'settings.html', context)
    

