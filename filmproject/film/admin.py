from django.contrib import admin
from film.models import FilmModel,ActorModel, CommentModel


admin.site.register(FilmModel)
admin.site.register(ActorModel)
admin.site.register(CommentModel)
