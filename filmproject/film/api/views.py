from rest_framework.generics import ListAPIView, RetrieveAPIView
from film.models import FilmModel,ActorModel
from film.api.serializers import Filmserializers,Actorserializers

class FilmListApiView(ListAPIView):
    queryset = FilmModel.objects.all()
    serializer_class = Filmserializers

class FilmRetrieveApiView(RetrieveAPIView):
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