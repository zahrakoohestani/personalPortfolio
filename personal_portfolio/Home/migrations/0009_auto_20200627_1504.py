# Generated by Django 3.0.7 on 2020-06-27 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0008_about_me'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='about_me',
            name='li_1',
        ),
        migrations.RemoveField(
            model_name='about_me',
            name='li_2',
        ),
        migrations.RemoveField(
            model_name='about_me',
            name='li_3',
        ),
        migrations.RemoveField(
            model_name='about_me',
            name='li_4',
        ),
        migrations.RemoveField(
            model_name='about_me',
            name='li_5',
        ),
        migrations.AlterField(
            model_name='about_me',
            name='first_caption',
            field=models.CharField(max_length=10000),
        ),
        migrations.AlterField(
            model_name='about_me',
            name='second_caption',
            field=models.CharField(max_length=10000),
        ),
    ]
