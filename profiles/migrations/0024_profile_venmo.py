# Generated by Django 2.0.6 on 2018-07-30 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0023_auto_20180729_2248'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='venmo',
            field=models.CharField(default='', max_length=100),
        ),
    ]
