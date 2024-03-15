from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register, name='blogRegister'),
    path('login/', views.login, name='blogLogin'),
]
