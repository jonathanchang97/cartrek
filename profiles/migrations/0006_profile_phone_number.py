# Generated by Django 2.0.6 on 2018-07-19 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='phone_number',
            field=models.CharField(default='555-555-555', max_length=17),
        ),
    ]