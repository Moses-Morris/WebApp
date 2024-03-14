from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm



# Create your views here.
def register(request):
    form = UserCreationForm()
    context = {
        'title': 'Register',
        'content': 'Welcome to the registration page',
        'form': form
    }
    return  render(request, 'register.html' , context)

def login(request):
    context = {
        'title': 'Login',
        'content': 'Welcome to the registration page'
    }
    return render(request, 'login.html', context)