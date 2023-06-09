from django.urls import path
from contact import views

urlpatterns = [
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('messages/',views.MessagesView.as_view(),name='messages')
]