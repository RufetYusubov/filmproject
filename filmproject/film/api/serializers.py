from  rest_framework import serializers
from film.models import FilmModel, ActorModel,CommentModel,LikeModel,Category,FavouriteFilms

class Filmserializer(serializers.ModelSerializer):
    class Meta:
        model = FilmModel
        fields = "__all__"

class FilmCreateserializer(serializers.ModelSerializer):
        class Meta:
            model = FilmModel
            exclude = ("views_count","rating")
#-----------------------------------------------------------------------------------

class Actorserializer(serializers.ModelSerializer):
        films = Filmserializer(many=True)
        class Meta:
            model = ActorModel
            fields = "__all__"

class ActorCreateserializer(serializers.ModelSerializer):
    class Meta:
        model = ActorModel
        fields = "__all__"
#--------------------------------------------------------------------------------

class Commentserializer(serializers.ModelSerializer):
        class Meta:
            model = CommentModel
            fields = "__all__"

class CommentCreateserializer(serializers.ModelSerializer):
    class Meta :
        model = CommentModel
        exclude = ("pub_date",)
#--------------------------------------------------------------------------------
class Likeserializer(serializers.ModelSerializer):
        class Meta:
             model = LikeModel
             fields = "__all__"

#-----------------------------------------------------------------------------------
class Categoryserializer(serializers.ModelSerializer):
     class Meta:
          model = Category
          fields = "__all__"
    
#------------------------------------------------------------------------------------
class FavouriteFilmssserializer(serializers.ModelSerializer):
     class Meta:
          model = FavouriteFilms
          fields = "__all__"


