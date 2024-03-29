# Generated by Django 4.2.1 on 2023-07-29 18:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ActorModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('birth_country', models.CharField(blank=True, max_length=100, null=True)),
                ('about', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Actor',
                'verbose_name_plural': 'Actors',
            },
        ),
        migrations.CreateModel(
            name='FilmModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('rating', models.FloatField(default=0)),
                ('pub_date', models.DateField(blank=True, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('poster', models.ImageField(upload_to='porters/')),
                ('video', models.FileField(upload_to='videos/')),
                ('views_count', models.IntegerField(default=0)),
                ('about', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Film',
                'verbose_name_plural': 'Films',
            },
        ),
        migrations.CreateModel(
            name='LikeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='actor_likes', to='film.actormodel')),
                ('film', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='film_likes', to='film.filmmodel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_likes', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'like',
            },
        ),
        migrations.CreateModel(
            name='FavouriteFilms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favourite_films', to='film.filmmodel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_favouritefilms', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'favourite film',
            },
        ),
        migrations.CreateModel(
            name='CommentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('actor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='actor_comments', to='film.actormodel')),
                ('film', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='film_comments', to='film.filmmodel')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='film.commentmodel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_comments', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Comment',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('films', models.ManyToManyField(related_name='film_categories', to='film.filmmodel')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.AddField(
            model_name='actormodel',
            name='films',
            field=models.ManyToManyField(related_name='actors', to='film.filmmodel'),
        ),
    ]
