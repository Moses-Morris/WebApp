from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages #messages.warning, messages. , messages.error, ,messages.success
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def register(request):
    if request.method == 'POST':
        #form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username') #form.cleaned_data['username'] #or ')
            messages.success(request, f'Account created for {username}!')
            return redirect('Login')
        else:
            messages.error(request, f'Account not created!')
    else:
        #form = UserCreationForm()
        form = UserRegisterForm()

    context = {
        'title': 'Register',
        'content': 'Welcome to the registration page',
        'form': form
    }
    return  render(request, 'register.html' , context)

@login_required
def profile(request):
    return render(request, 'profile.html')