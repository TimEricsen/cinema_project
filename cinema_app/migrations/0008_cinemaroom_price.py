# Generated by Django 4.2 on 2023-04-14 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema_app', '0007_alter_order_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='cinemaroom',
            name='price',
            field=models.IntegerField(default=50, verbose_name='Ticket Price'),
            preserve_default=False,
        ),
    ]
