# Generated by Django 2.0.6 on 2018-07-24 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0016_auto_20180723_1157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='vehicle',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
    ]