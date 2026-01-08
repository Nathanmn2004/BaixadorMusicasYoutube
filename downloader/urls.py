

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('download_audio/', views.download_audio, name='download_audio'),
]
