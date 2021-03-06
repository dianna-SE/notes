# Generated by Django 4.0.3 on 2022-05-27 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vue_app', '0010_post_coursename_post_filename'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='coursename',
        ),
        migrations.RemoveField(
            model_name='post',
            name='filename',
        ),
        migrations.AddField(
            model_name='post',
            name='course_name',
            field=models.TextField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='post',
            name='file_name',
            field=models.TextField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='post',
            name='caption',
            field=models.TextField(max_length=80),
        ),
    ]
