# Generated by Django 2.0.6 on 2018-07-22 23:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0014_auto_20180722_1300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='affiliation',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.PROTECT, to='profiles.Organization'),
        ),
    ]
