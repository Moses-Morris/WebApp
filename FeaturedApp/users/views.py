from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages #messages.warning, messages. , messages.error, ,messages.success


# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username') #form.cleaned_data['username'] #or ')
            messages.success(request, f'Account created for {username}!')
            return redirect('blogLogin')
        else:
            messages.error(request, f'Account not created!')
    else:
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