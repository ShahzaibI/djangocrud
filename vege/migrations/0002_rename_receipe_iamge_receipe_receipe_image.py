# Generated by Django 5.0.6 on 2024-05-29 06:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='receipe',
            old_name='receipe_iamge',
            new_name='receipe_image',
        ),
    ]