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
    path('actor-retrieve/<int:pk>/',views.ActorRetrieveApiView.as_view(), name="actor"),
    path('actor-create/',views.ActorCreateApi.as_view(),name="actor-create"),
    path('actor-update/<int:pk>/',views.ActorUpdateApiView.as_view(),name="actor-update"),
    path('actor-delete/<int:pk>/',views.ActorDestroyApiView.as_view(),name="actor-delete"),

    path('comments/',views.CommentListApiView.as_view(),name="comments"),
    path('comment/<int:pk>/',views.CommentRetrieveApiView.as_view(),name="comment"),
    path('comment-create/', views.CommentCreateApiView.as_view(),name="comment-create"),
    path('comment-update/<int:pk>',views.CommentUpdateApiView.as_view(),name="comment-update"),
    path('comment-delete/<int:pk>',views.CommentDestroyApiView.as_view(),name="comment-delete"),
    path('comment-retrieve-update-delete/<int:pk>',views.CommentRetrieveUpdateDestroyApiView.as_view(),name="commment-retrieve-update-delete"),

    path('likes-list-create/',views.LikeListCreateApiView.as_view(),name="likes"),
    path('like-retrieve-update-delete/<int:pk>/',views.LikeRetrieveUpdateDestroyApiView.as_view(),name="like-retrieve-update-destroy"),


    path('categories-list-create/',views.CategoryListCreateApiView.as_view()),
    path('category-retrieve-update-delete/',views.CategoryRetrieveUpdateDestroy.as_view()),

    path('favouritefilms-list-create/',views.FavouriteFilmsListCreateApiView.as_view()),
    path('favouritefilm-retrieve-update-delete/',views.FavouriteFilmsRetrieveUpdateDestroy.as_view())

]