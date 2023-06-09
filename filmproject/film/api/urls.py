from django.urls import path
from film.api import views

urlpatterns = [
    path("films/",views.FilmListApiView.as_view(),name="films"),
    path('film/<int:pk>/',views.FilmRetrieveApiView.as_view(),name = "film"),
    path('actors/',views.ActorListApiView.as_view(),name="actors"),
    path('actor/<int:pk>/',views.ActorRetrieveApiView.as_view(), name="actor")
]