# Generated by Django 2.0.6 on 2018-07-26 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0018_auto_20180724_1525'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='domain',
            field=models.CharField(default='tufts.edu', max_length=50),
        ),
    ]
