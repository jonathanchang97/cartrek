from django.test import TestCase
from django.contrib.auth.models import User

from .models import Profile

class UserProfileTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        u = User.objects.create_user('test', 'email', 'password')

    def test_pic_label(self):
        p = Profile.objects.get(id=1)
        flabel = p._meta.get_field('picture').verbose_name
        self.assertEquals(flabel, 'picture')
