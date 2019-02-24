from django.test import TestCase
from django.contrib.auth.models import User

from .models import Trek

class TrekTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        u = User.objects.create_user('test', 'email', 'password')
        t = Trek.objects.create(driver=u)

    def test_trek_driver_label(self):
        t = Trek.objects.get(id=1)
        flabel = t._meta.get_field('driver').verbose_name
        self.assertEquals(flabel, 'driver')
