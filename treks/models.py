from datetime import date

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Trek(models.Model):
    driver = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='driver')
    passengers = models.ManyToManyField(User, related_name='passengers', blank=True)
    date = models.DateField(default=date.today)
    departure_time = models.TimeField(default=timezone.now)
    flexible_departure = models.BooleanField(default=True)
    arrival_time = models.TimeField(default=timezone.now)
    from_addr = models.CharField(max_length=100, default='', blank=True)
    from_city = models.CharField(max_length=100, default='Medford')
    from_state = models.CharField(max_length=2, default='MA')
    to_addr = models.CharField(max_length=100, default='', blank=True)
    to_city = models.CharField(max_length=100, default='Woodstock')
    to_state = models.CharField(max_length=100, default='NH')
    pickup = models.BooleanField(default=False)
    pickup_radius = models.IntegerField(default=5)
    dropoff = models.BooleanField(default=False)
    dropoff_radius = models.IntegerField(default=5)
    price = models.IntegerField(default='20')
    note = models.TextField(default='')
    seats = models.IntegerField(default='3')
    fem_only = models.BooleanField(default=False)
    org_only = models.BooleanField(default=False)
    edu_only = models.BooleanField(default=False)
    mutuals_only = models.BooleanField(default=False)

class Request(models.Model):
    passenger = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='passenger', default=1)
    date = models.DateField(default=date.today)
    departure_time = models.TimeField(default=timezone.now)
    flexible_departure = models.BooleanField(default=True)
    arrival_time = models.TimeField(default=timezone.now)
    from_addr = models.CharField(max_length=100, default='', blank=True)
    from_city = models.CharField(max_length=100, default='Medford')
    from_state = models.CharField(max_length=2, default='MA')
    to_addr = models.CharField(max_length=100, default='', blank=True)
    to_city = models.CharField(max_length=100, default='Woodstock')
    to_state = models.CharField(max_length=100, default='NH')
    pickup = models.BooleanField(default=False)
    pickup_radius = models.IntegerField(default=5)
    dropoff = models.BooleanField(default=False)
    dropoff_radius = models.IntegerField(default=5)
    note = models.TextField(default='')
    fem_only = models.BooleanField(default=False)
    org_only = models.BooleanField(default=False)
    edu_only = models.BooleanField(default=False)
    mutuals_only = models.BooleanField(default=False)
