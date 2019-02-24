from django.urls import path

from . import views

urlpatterns = [
    path('all/', views.view_all, name='alltreks'),
    path('some/', views.view_some, name='sometreks'),
    path('post/', views.post, name='post_trek'),
    path('request/', views.request_trek, name='request_trek'),
    path('join/<int:trekid>/', views.join, name='join'),
    path('delete/<int:trekid>/', views.delete, name='delete'),
    path('leave/<int:trekid>/', views.leave, name='leave'),
    path('<int:trekid>/', views.trek, name='viewtrek'),
]
