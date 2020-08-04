# Generated by Django 3.0.8 on 2020-08-01 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0007_auto_20200801_0636'),
    ]

    operations = [
        migrations.AddField(
            model_name='parentprofile',
            name='gradelevel',
            field=models.CharField(default='', max_length=20, verbose_name='gradelevel'),
        ),
        migrations.AddField(
            model_name='studentprofile',
            name='gradelevel',
            field=models.CharField(default='', max_length=20, verbose_name='gradelevel'),
        ),
        migrations.AddField(
            model_name='teacherprofile',
            name='gradelevel',
            field=models.CharField(default='', max_length=20, verbose_name='gradelevel'),
        ),
        migrations.AlterField(
            model_name='parentprofile',
            name='name',
            field=models.CharField(default='', max_length=100, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='parentprofile',
            name='school',
            field=models.CharField(default='', max_length=255, verbose_name='school'),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='name',
            field=models.CharField(default='', max_length=100, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='school',
            field=models.CharField(default='', max_length=255, verbose_name='school'),
        ),
        migrations.AlterField(
            model_name='teacherprofile',
            name='name',
            field=models.CharField(default='', max_length=100, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='teacherprofile',
            name='school',
            field=models.CharField(default='', max_length=255, verbose_name='school'),
        ),
    ]