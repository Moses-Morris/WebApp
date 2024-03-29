from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.register, name='Register'),
    path('register/', views.register, name='Register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='Login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='Logout'),
    path('profile/', views.profile, name='Profile'),
]
