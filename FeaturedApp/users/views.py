from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages #messages.warning, messages. , messages.error, ,messages.success
from .forms import UserRegisterForm, userUpdateForm, userUpdateProfile
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
    if request.method == 'POST':
        u_form = userUpdateForm(request.POST, instance=request.user)
        p_form = userUpdateProfile(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            
    else:
        u_form = userUpdateForm(instance=request.user)
        p_form = userUpdateProfile(instance=request.user.profile)
        messages.error(request, f'Your account not Update!')


    context = {
        'title': 'Profile',
        'content': 'Welcome to the profile page',
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'profile.html', context)

