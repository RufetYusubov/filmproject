from django.db import models
from django.contrib.auth.models import User

class FilmModel(models.Model):
    name = models.CharField(max_length=500)
    rating = models.FloatField(default = 0)
    pub_date = models.DateField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    production_country = models.CharField(max_length=300,blank=True,null=True)
    movie_duration = models.CharField(max_length=300,blank=True,null=True)
    poster = models.ImageField(upload_to = 'porters/')
    video = models.FileField(upload_to = 'videos/')
    views_count = models.IntegerField(default=0)
    about = models.TextField(blank = True, null = True)

    class Meta:
        verbose_name = "Film"
        verbose_name_plural = "Films"

    def __str__(self) :
        return self.name
#----------------------------------------------------------
    
class Category(models.Model):
    films = models.ManyToManyField(FilmModel,related_name="film_categories")
    name = models.CharField(max_length=100)


    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self) -> str:
        return self.name
    
#-----------------------------------------------------------------    
class ActorModel(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='actors_photos',blank=True,null=True)
    birth_date = models.DateField(blank=True, null=True)
    birth_country = models.CharField(max_length=100,blank=True, null=True)
    about = models.TextField(blank=True,null=True)
    films = models.ManyToManyField(FilmModel,related_name="actors")

    class Meta:
        verbose_name = "Actor"
        verbose_name_plural = "Actors"

    def __str__(self):
        return self.name + " " + self.surname
    
#---------------------------------------------------------------------------------------
class CommentModel(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE, related_name="user_comments")
    film = models.ForeignKey(FilmModel,on_delete=models.CASCADE,blank=True, null=True,related_name="film_comments")
    actor = models.ForeignKey(ActorModel, on_delete=models.CASCADE,blank=True, null=True, related_name="actor_comments")
    parent = models.ForeignKey("self", on_delete=models.CASCADE,blank=True,null=True,related_name="replies")
    comment = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Comment"
        ordering = ("id",)

    def __str__(self):
        return self.user.username + " " + str(self.id)
#--------------------------------------------------------------------
class LikeModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_likes")
    film = models.ForeignKey(FilmModel,on_delete=models.CASCADE,blank=True, null=True,related_name="film_likes")
    actor = models.ForeignKey(ActorModel, on_delete=models.CASCADE,blank=True, null=True,related_name="actor_likes")
    
    class Meta:
        verbose_name = "like"

    def __str__(self):
        return self.user.username + " " + str(self.id)
#----------------------------------------------------
class FavouriteFilms(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_favouritefilms")
    film = models.ForeignKey(FilmModel, on_delete=models.CASCADE, related_name="favourite_films")

    class Meta:
        verbose_name = "favourite film"

    
    def __str__(self) :
        return  self.user.username