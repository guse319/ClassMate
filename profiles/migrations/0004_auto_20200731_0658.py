# Generated by Django 3.0.8 on 2020-07-31 06:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_myuser_type'),
        ('profiles', '0003_auto_20200731_0606'),
    ]

    operations = [
        migrations.CreateModel(
            name='ParentProfile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('school', models.CharField(default='school', max_length=255, verbose_name='school')),
                ('name', models.CharField(default='name', max_length=100, verbose_name='name')),
            ],
        ),
        migrations.CreateModel(
            name='TeacherProfile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('school', models.CharField(default='school', max_length=255, verbose_name='school')),
                ('name', models.CharField(default='name', max_length=100, verbose_name='name')),
            ],
        ),
        migrations.AddField(
            model_name='studentprofile',
            name='name',
            field=models.CharField(default='name', max_length=100, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='school',
            field=models.CharField(default='school', max_length=255, verbose_name='school'),
        ),
        migrations.AlterField(
            model_name='tutorprofile',
            name='name',
            field=models.CharField(default='name', max_length=100, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='tutorprofile',
            name='school',
            field=models.CharField(default='school', max_length=100, verbose_name='school'),
        ),
    ]