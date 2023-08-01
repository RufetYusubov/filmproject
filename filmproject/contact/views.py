from django.shortcuts import render,redirect
from contact.models import ContactModel
from django.contrib import messages
from django.http import Http404
from film.models import Category
from django.views import View
class ContactView(View):
    def get(self,request,*args,**kwargs):
        categories = Category.objects.all()
        self.context = {
            "categories" : categories
        }
        return render(request,'contact.html', self.context)
    
    def post(self,request,*args,**kwargs):
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        email = request.POST.get('email')
        telephone = request.POST.get('telephone')
        message = request.POST.get('message')

        ContactModel.objects.create(
            name = name,
            surname = surname,
            email = email,
            telephone = telephone,
            message = message
        )
        messages.success(request, "Message sent")
        
        return redirect("contact")
#---------------------------------------------------------------------------
class MessagesView(View):
    def get(self,request,*args,**kwargs):
        if not request.user.is_staff:
            raise Http404
        categories = Category.objects.all()
        messages = ContactModel.objects.order_by("-id")
        context = {
            "messages" : messages,
            "categories" : categories
        }
        return render(request,'messages.html',context)