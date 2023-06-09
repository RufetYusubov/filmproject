from  rest_framework import serializers
from film.models import FilmModel, ActorModel

class Filmserializers(serializers.ModelSerializer):
    class Meta:
        model = FilmModel
        fields = "__all__"
class Actorserializers(serializers.ModelSerializer):
    films = Filmserializers(many=True)
    class Meta:
        model = ActorModel
        fields = "__all__"