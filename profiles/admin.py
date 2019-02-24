from django.contrib import admin

from .models import Profile, Organization, Message, Car

admin.site.register(Profile)
admin.site.register(Organization)
admin.site.register(Message)
admin.site.register(Car)
