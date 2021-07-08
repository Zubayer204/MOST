from django.urls import path
from . import views


urlpatterns = [
    path('subscribe/', views.subscribe, name='subscribe'),
    path('visitor/', views.track_visitor, name='visitor'),
]
