from rest_framework.generics import (ListAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView,
                                      CreateAPIView,UpdateAPIView,DestroyAPIView,ListCreateAPIView)
from film.models import FilmModel,ActorModel,CommentModel,LikeModel,Category,FavouriteFilms
from film.api.serializers import (Filmserializer,FilmCreateserializer,
                            Actorserializer, ActorCreateserializer,
                            Commentserializer,CommentCreateserializer,
                            Likeserializer,Categoryserializer,FavouriteFilmssserializer)

class FilmListApiView(ListAPIView):
    queryset = FilmModel.objects.all()
    serializer_class = Filmserializer

class FilmRetrieveApiView(RetrieveAPIView):
    queryset = FilmModel.objects.all()
    serializer_class = Filmserializer
    lookup_field = "pk"

class FilmCreateApiView(CreateAPIView):
    queryset = FilmModel.objects.all()
    serializer_class = FilmCreateserializer

class FilmUpdateApiView(UpdateAPIView):
      queryset = FilmModel.objects.all()
      serializer_class = Filmserializer
      lookup_field = "pk"

class FilmDestroyApiView(DestroyAPIView):
     queryset = FilmModel.objects.all()
     serializer_class = Filmserializer
     lookup_field = "pk"


class FilmRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
     queryset = FilmModel.objects.all()
     serializer_class = Filmserializer
     lookup_field = "pk"

#--------------------------------------------------------------------------------------------------
class ActorListApiView(ListAPIView):
    queryset = ActorModel.objects.all()
    serializer_class = Actorserializer

class ActorRetrieveApiView(RetrieveAPIView):
    queryset = ActorModel.objects.all()
    serializer_class = Actorserializer
    lookup_field = "pk"

class ActorCreateApi(CreateAPIView):
      queryset = ActorModel.objects.all()
      serializer_class = ActorCreateserializer

class ActorUpdateApiView(UpdateAPIView):
       queryset = ActorModel.objects.all()
       serializer_class = Actorserializer
       lookup_field = "pk"

class ActorDestroyApiView(DestroyAPIView):
        queryset = ActorModel.objects.all()
        serializer_class = Actorserializer
        lookup_field = "pk"
#--------------------------------------------------------------------------------------------------------


class CommentListApiView(ListAPIView):
    queryset = CommentModel.objects.all()
    serializer_class = Commentserializer

class CommentRetrieveApiView(RetrieveAPIView):
    queryset = CommentModel.objects.all()
    serializer_class = Commentserializer
    lookup_field = "pk"

class CommentCreateApiView(CreateAPIView):
     queryset = CommentModel.objects.all()
     serializer_class = CommentCreateserializer

class CommentUpdateApiView(UpdateAPIView):
     queryset = CommentModel.objects.all()
     serializer_class = Commentserializer
     lookup_field = "pk"

class CommentDestroyApiView(DestroyAPIView):
     queryset = CommentModel.objects.all()
     serializer_class = Commentserializer
     lookup_field = "pk"

class CommentRetrieveUpdateDestroyApiView(RetrieveUpdateDestroyAPIView):
     queryset = CommentModel.objects.all()
     serializer_class = Commentserializer
     lookup_field = "pk"

#--------------------------------------------------------------------------------------
class LikeListCreateApiView(ListCreateAPIView):
     queryset = LikeModel.objects.all()
     serializer_class = Likeserializer

class LikeRetrieveUpdateDestroyApiView(RetrieveUpdateDestroyAPIView):
     queryset = LikeModel.objects.all()
     serializer_class = Likeserializer
     lookup_field = "pk"
    
#---------------------------------------------------------------------------------------------
class CategoryListCreateApiView(ListCreateAPIView):
     queryset = Category.objects.all()
     serializer_class = Categoryserializer
    
class CategoryRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
     queryset = Category.objects.all()
     serializer_class = Categoryserializer
    
#--------------------------------------------------------------------------------------------
class FavouriteFilmsListCreateApiView(ListCreateAPIView):
     queryset = FavouriteFilms.objects.all()
     serializer_class = FavouriteFilmssserializer
    
class FavouriteFilmsRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
     queryset = FavouriteFilms.objects.all()
     serializer_class = FavouriteFilmssserializer



     
