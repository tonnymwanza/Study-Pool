# Generated by Django 4.1 on 2024-04-28 17:46

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='likes',
            field=models.ManyToManyField(null=True, related_name='user_likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
