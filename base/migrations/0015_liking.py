# Generated by Django 3.2.7 on 2024-04-02 02:21

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0014_room_rules'),
    ]

    operations = [
        migrations.CreateModel(
            name='Liking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like', models.ManyToManyField(related_name='user_likes', to=settings.AUTH_USER_MODEL)),
                ('room', models.ManyToManyField(to='base.Room')),
                ('unlike', models.ManyToManyField(related_name='user_unlikes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]