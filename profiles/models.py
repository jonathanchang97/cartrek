from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
#from django.core.validators import RegexValidator

class Car(models.Model):
    make = models.CharField(max_length=100, default='Honda')
    model = models.CharField(max_length=100, default='Civic')
    plate = models.CharField(max_length=10, default='XXX-XXXX')

    def __str__(self):
        return ' '.join([self.make, self.model])

class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sender', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='receiver', on_delete=models.CASCADE)
    content = models.TextField(default='')
    timestamp = models.DateTimeField(default=timezone.now)
    read = models.BooleanField(default=False)

class Organization(models.Model):
    name = models.CharField(default='Tufts University', max_length=100)
    domain = models.CharField(default='tufts.edu', max_length=50)

    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    affiliation = models.ForeignKey(Organization, blank=True, null=True, on_delete=models.PROTECT)
    org_email = models.CharField(default='', max_length=100)
    verified = models.BooleanField(default=False)
    hometown = models.CharField(default='', max_length=100)
    major = models.CharField(default='', max_length=100, blank=True, null=True)
    bio = models.TextField(default='')
    picture = models.CharField(default='default.png', max_length=100)
    venmo = models.CharField(default='', max_length=100)
    car = models.OneToOneField(Car, null=True, default=None, on_delete=models.CASCADE)
#   vehicle = models.CharField(default='', max_length=100, blank=True, null=True)
#   phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message='format: +999999999')
#   phone_number = CharField(validators=[phone_regex], max_length=17, default='+555555555')
    phone_number = models.CharField(max_length=17, default='555-555-5555')

    def __str__(self):
        return self.user.get_username()
