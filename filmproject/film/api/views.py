from rest_framework.generics import (ListAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView,
                                      CreateAPIView,UpdateAPIView,DestroyAPIView)
from film.models import FilmModel,ActorModel,CommentModel
from film.api.serializers import (Filmserializers,FilmCreateserializers,
                            Actorserializers, ActorCreateserializer,
                            Commentserializers)

class FilmListApiView(ListAPIView):
    queryset = FilmModel.objects.all()
    serializer_class = Filmserializers

class FilmRetrieveApiView(RetrieveAPIView):
    queryset = FilmModel.objects.all()
    serializer_class = Filmserializers
    lookup_field = "pk"

class FilmCreateApiView(CreateAPIView):
    queryset = FilmModel.objects.all()
    serializer_class = FilmCreateserializers

class FilmUpdateApiView(UpdateAPIView):
      queryset = FilmModel.objects.all()
      serializer_class = Filmserializers
      lookup_field = "pk"

class FilmDestroyApiView(DestroyAPIView):
     queryset = FilmModel.objects.all()
     serializer_class = Filmserializers
     lookup_field = "pk"

class ActorListApiView(ListAPIView):
    queryset = ActorModel.objects.all()
    serializer_class = Actorserializers

class ActorRetrieveApiView(RetrieveAPIView):
    queryset = ActorModel.objects.all()
    serializer_class = Actorserializers
    lookup_field = "pk"

class ActorCreateApi(CreateAPIView):
      queryset = ActorModel.objects.all()
      serializer_class = ActorCreateserializer

class ActorUpdateApiView(UpdateAPIView):
       queryset = ActorModel.objects.all()
       serializer_class = Actorserializers
       lookup_field = "pk"

class ActorDestroyApiView(DestroyAPIView):
        queryset = ActorModel.objects.all()
        serializer_class = Actorserializers
        lookup_field = "pk"


class FilmRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
     queryset = FilmModel.objects.all()
     serializer_class = Filmserializers
     lookup_field = "pk"

class CommentListApiView(ListAPIView):
    queryset = CommentModel.objects.all()
    serializer_class = Commentserializers

class CommentRetrieveApiView(RetrieveAPIView):
    queryset = CommentModel.objects.all()
    serializer_class = Commentserializers
    lookup_field = "pk"