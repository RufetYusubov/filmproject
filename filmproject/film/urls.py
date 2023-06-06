from django.urls import path
from film import views
urlpatterns = [
    path('index/', views.IndexView.as_view(), name='index'),
    path('detail/<int:id>/', views.DetailView.as_view(), name="detail"),
    path('actors/<int:id>/',views.actors,name="actors"),
    path('delete/<int:id>/' ,views.deleteComment,name="delete_comment"),
    path('deleteactor/<int:id>/' ,views.deleteactorComment,name="delete_actor_comment"),
    path('category/<int:id>/',views.Categoryfilms.as_view(), name="categoryfilms"),
    path('myfavouritefilms/',views.favouritefilms,name = "myfavouritefilms"),
]