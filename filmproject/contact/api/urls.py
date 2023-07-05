from django.urls import path
from contact.api import views

urlpatterns = [
    path('contact-list-create/',views.ContactListCreateApiView.as_view()),
    path('contact-retrieve-update-delete/<int:pk>/',views.ContactRetrieveUpdateDestroy.as_view())
]