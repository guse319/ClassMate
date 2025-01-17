# Generated by Django 3.0.8 on 2020-08-01 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_auto_20200801_0135'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutorprofile',
            name='accommodations',
            field=models.CharField(default='', max_length=50, verbose_name='accommodations'),
        ),
        migrations.AlterField(
            model_name='tutorprofile',
            name='clients',
            field=models.CharField(default='', max_length=50, verbose_name='clients'),
        ),
        migrations.AlterField(
            model_name='tutorprofile',
            name='major',
            field=models.CharField(default='', max_length=50, verbose_name='major'),
        ),
        migrations.AlterField(
            model_name='tutorprofile',
            name='name',
            field=models.CharField(default='', max_length=100, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='tutorprofile',
            name='school',
            field=models.CharField(default='', max_length=100, verbose_name='school'),
        ),
        migrations.AlterField(
            model_name='tutorprofile',
            name='subjects',
            field=models.TextField(default='', max_length=400, verbose_name='subjects'),
        ),
    ]
