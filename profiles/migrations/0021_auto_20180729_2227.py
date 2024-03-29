# Generated by Django 2.0.6 on 2018-07-30 02:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0020_auto_20180726_1336'),
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
        migrations.RemoveField(
            model_name='profile',
            name='vehicle',
        ),
        migrations.AddField(
            model_name='profile',
            name='car',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='profiles.Car'),
        ),
    ]
