# Generated by Django 4.2 on 2023-04-11 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cinemapremiere',
            name='duration',
            field=models.CharField(default='2h 1m', max_length=250, verbose_name='Duration'),
            preserve_default=False,
        ),
    ]