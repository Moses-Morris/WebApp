from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='blogHome'),
    path('about/', views.about, name='blogAbout'),
]
