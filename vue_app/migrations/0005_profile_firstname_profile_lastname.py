# Generated by Django 4.0.3 on 2022-05-21 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vue_app', '0004_alter_profile_profileimg'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='firstname',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='profile',
            name='lastname',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
