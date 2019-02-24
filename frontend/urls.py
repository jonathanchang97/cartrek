from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/browse/', permanent=True)),
    path('browse/', views.browse, name='browse'),
    path('post/', views.post, name='post'),
    path('request/', views.request, name='request'),
    path('blog/', views.blog, name='blog'),
    path('about/', views.about, name='about'),
    path('accounts/', include('allauth.urls')),
    path('profile/<str:user>/', views.profile, name='profile'),
    path('treks/', include('treks.urls')),
    path('profiles/', include('profiles.urls')),
    path('create/', views.create_profile, name='create'),
    path('edit/', views.edit_profile, name='edit'),
    path('inbox/', views.inbox, name='inbox'),
    path('msg/<str:user>', views.send_msg, name='sendmsg'),
    path('trek/<int:trekid>/', views.trek, name='trek'),
    path('login/', views.login, name='login'),
    path('terms/', views.terms, name='terms'),
    path('privacy/', views.privacy, name='privacy'),
]
