# Generated by Django 4.2 on 2023-04-27 08:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='filmname',
            new_name='FilmModel',
        ),
    ]
