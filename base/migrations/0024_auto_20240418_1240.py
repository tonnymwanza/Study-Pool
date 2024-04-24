# Generated by Django 3.2.7 on 2024-04-18 12:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0023_auto_20240418_1219'),
    ]

    operations = [
        migrations.AddField(
            model_name='follow',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='follow',
            name='follower',
            field=models.ManyToManyField(related_name='the_follower', to=settings.AUTH_USER_MODEL),
        ),
    ]