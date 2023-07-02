from  rest_framework import serializers
from film.models import FilmModel, ActorModel,CommentModel

class Filmserializers(serializers.ModelSerializer):
    class Meta:
        model = FilmModel
        fields = "__all__"

class FilmCreateserializers(serializers.ModelSerializer):
    class Meta:
        model = FilmModel
        exclude = ("views_count",)

class Actorserializers(serializers.ModelSerializer):
    films = Filmserializers(many=True)
    class Meta:
        model = ActorModel
        fields = "__all__"

class ActorCreateserializer(serializers.ModelSerializer):
    class Meta:
        model = ActorModel
        fields = "__all__"

class Commentserializers(serializers.ModelSerializer):
    class Meta:
        model = CommentModel
        fields = "__all__"