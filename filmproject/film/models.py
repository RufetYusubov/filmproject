from django.db import models

class FilmModel(models.Model):
    name = models.CharField(max_length=500)
    rating = models.FloatField(default = 0)
    pub_date = models.DateTimeField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    poster = models.ImageField(upload_to = 'porters/')
    video = models.FileField(upload_to = 'videos/')
    views_count = models.IntegerField(default=0)
    about = models.TextField(blank = True, null = True)

    class Meta:
        verbose_name = "Film"
        verbose_name_plural = "Films"

    def __str__(self) :
        return self.name
    
class ActorModel(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    birth_date = models.DateField(blank=True, null=True)
    birth_country = models.CharField(max_length=100,blank=True, null=True)
    about = models.TextField(blank=True,null=True)
    films = models.ManyToManyField(FilmModel,related_name="actors")

    class Meta:
        verbose_name = "Actor"
        verbose_name_plural = "Actors"

    def __str__(self):
        return self.name + " " + self.surname