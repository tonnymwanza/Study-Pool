# Generated by Django 4.1 on 2024-04-10 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0019_alter_message_body_alter_message_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='body',
            field=models.TextField(null=True),
        ),
    ]
