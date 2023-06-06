# Generated by Django 4.2.1 on 2023-06-02 15:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('film', '0009_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='FavouriteFilms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favourite_films', to='film.filmmodel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_favouritefilms', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
