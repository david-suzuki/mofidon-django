# Generated by Django 3.1.13 on 2021-10-09 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20211009_0334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(blank=True, default='Username', max_length=255, unique=True, verbose_name='Username of User'),
        ),
    ]
