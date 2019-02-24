from django.urls import path

from . import views

urlpatterns = [
    path('edit/', views.edit, name='edit'),
    path('readmsg/<int:m_id>/', views.readmsg, name='readmsg'),
    path('msg_count/', views.msg_count, name='msg_count'),
    path('sendmsg/', views.sendmsg, name='sendmsg'),
    path('<str:user>/', views.profile, name='profiles'),
]
