# Generated by Django 2.0.6 on 2018-07-30 04:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('treks', '0016_request'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='passenger',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='passenger', to=settings.AUTH_USER_MODEL),
        ),
    ]
