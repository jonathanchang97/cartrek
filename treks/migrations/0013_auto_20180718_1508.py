# Generated by Django 2.0.6 on 2018-07-18 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('treks', '0012_auto_20180718_1411'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trek',
            name='destination',
        ),
        migrations.RemoveField(
            model_name='trek',
            name='source',
        ),
        migrations.AddField(
            model_name='trek',
            name='from_addr',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='trek',
            name='from_city',
            field=models.CharField(default='Medford', max_length=100),
        ),
        migrations.AddField(
            model_name='trek',
            name='from_state',
            field=models.CharField(default='MA', max_length=2),
        ),
        migrations.AddField(
            model_name='trek',
            name='to_addr',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='trek',
            name='to_city',
            field=models.CharField(default='Woodstock', max_length=100),
        ),
        migrations.AddField(
            model_name='trek',
            name='to_state',
            field=models.CharField(default='NH', max_length=100),
        ),
        migrations.AlterField(
            model_name='trek',
            name='dropoff_radius',
            field=models.IntegerField(default=5),
        ),
        migrations.AlterField(
            model_name='trek',
            name='flexible_departure',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='trek',
            name='pickup_radius',
            field=models.IntegerField(default=5),
        ),
    ]
