from django.urls import path
from film.api import views

urlpatterns = [
    path('films/',views.FilmListApiView.as_view(),name="films"),
    path('film/<int:pk>/',views.FilmRetrieveApiView.as_view(),name = "film"),
    path('film-create/',views.FilmCreateApiView.as_view(),name="film-create"),
    path('film-update/<int:pk>/',views.FilmUpdateApiView.as_view(),name="film-update"),
    path('film-delete/<int:pk>/',views.FilmDestroyApiView.as_view(),name = "film-delete"),
    path('film-retrieve-update-delete/<int:pk>/',views.FilmRetrieveUpdateDestroyAPIView.as_view(),name="film-retrieve-update-delete"),

    path('actors/',views.ActorListApiView.as_view(),name="actors"),
    path('actor/<int:pk>/',views.ActorRetrieveApiView.as_view(), name="actor"),
    path('actor-create/',views.ActorCreateApi.as_view(),name="actor-create"),
    path('actor-update/<int:pk>/',views.ActorUpdateApiView.as_view(),name="actor-update"),
    path('actor-delete/<int:pk>/',views.ActorDestroyApiView.as_view(),name="actor-delete"),

    path('comments/',views.CommentListApiView.as_view(),name="comments"),
    path('comment/<int:pk>/',views.CommentRetrieveApiView.as_view(),name="comment"),
    

]