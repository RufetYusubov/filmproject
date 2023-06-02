from django.urls import path
from film import views
urlpatterns = [
    path('index/', views.index, name='index'),
    path('detail/<int:id>/', views.detail, name="detail"),
    path('actors/<int:id>/',views.actors,name="actors"),
    path('delete/<int:id>/' ,views.deleteComment,name="delete_comment"),
    path('deleteactor/<int:id>/' ,views.deleteactorComment,name="delete_actor_comment"),
    path('category/<int:id>/',views.categoryfilms, name="categoryfilms")
]