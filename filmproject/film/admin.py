from django.contrib import admin
from film.models import FilmModel,ActorModel, CommentModel, LikeModel, Category


admin.site.register(FilmModel)
admin.site.register(ActorModel)
admin.site.register(CommentModel)
admin.site.register(LikeModel)
admin.site.register(Category)
