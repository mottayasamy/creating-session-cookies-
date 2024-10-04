from django.urls import path
from . import views

urlpatterns = [
    path('set_session/', views.set_session, name='set_session'),
    path('get_session/', views.get_session, name='get_session'),
    path('set_cookie/', views.set_cookie, name='set_cookie'),
    path('get_cookie/', views.get_cookie, name='get_cookie'),
]
