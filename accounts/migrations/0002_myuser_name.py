# Generated by Django 3.0.8 on 2020-07-27 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='name',
            field=models.CharField(default='no name', max_length=255, verbose_name='name'),
        ),
    ]