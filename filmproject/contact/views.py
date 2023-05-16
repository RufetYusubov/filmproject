from django.shortcuts import render
from contact.models import ContactModel
from django.contrib import messages
def contact(request):
    if request.method == "POST":
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

    return render(request,'contact.html')
