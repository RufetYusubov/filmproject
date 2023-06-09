from django.contrib import admin
from film.models import FilmModel,ActorModel, CommentModel, LikeModel, Category, FavouriteFilms

@admin.register(FilmModel)
class FilmAdmin(admin.ModelAdmin):
    list_display = ("name","rating","pub_date")
    list_display_links = ("name","rating")
    list_editable = ("pub_date",)
    list_filter = ("pub_date",)
    search_fields = ("name",)
    fieldsets = [
         (
            "Basic options",
            {
                "fields": ["name", "rating", "pub_date"],
            },
        ),
        (
            "Advanced options",
            {
                "classes": ["video"],
                "fields": ["views_count", "about"],
            },
        ),
    ]
# admin.site.register(FilmModel,FilmAdmin)
admin.site.register(ActorModel)
admin.site.register(CommentModel)
admin.site.register(LikeModel)
admin.site.register(Category)
admin.site.register(FavouriteFilms)

admin.sites.AdminSite.site_title = "Film Adminstration"
admin.sites.AdminSite.site_header = "Film Adminstration"