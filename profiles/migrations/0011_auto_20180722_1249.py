# Generated by Django 2.0.6 on 2018-07-22 16:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0010_auto_20180722_1245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='timestamp',
            field=models.TimeField(default=datetime.datetime.today),
        ),
    ]