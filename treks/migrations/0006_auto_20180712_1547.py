# Generated by Django 2.0.6 on 2018-07-12 19:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('treks', '0005_auto_20180710_1242'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(default='Nissan', max_length=100)),
                ('model', models.CharField(default='Versa', max_length=100)),
                ('year', models.IntegerField(default=2012)),
                ('plate', models.CharField(default='JBZ-5775', max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='trek',
            name='price',
            field=models.IntegerField(default='5'),
        ),
        migrations.AddField(
            model_name='trek',
            name='vehicle',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.PROTECT, to='treks.Car'),
        ),
    ]
