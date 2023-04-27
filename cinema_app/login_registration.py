from .forms import LoginForm, RegisterForm

from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate


def login_context(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('main_page')
        else:
            for error in form.errors:
                messages.error(request, form.errors[error].as_text())
            return redirect('login')
    else:
        form = LoginForm()
        context = {
            'title': 'Login',
            'form': form
        }
        return render(request, 'login.html', context)


def register_context(request):
    if request.method == 'POST':
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            new_user = authenticate(username=form.cleaned_data['username'],
                                    email=form.cleaned_data['email'],
                                    password=form.cleaned_data['password1'])
            login(request, new_user)
            messages.success(request, 'You have successfully registered!')
            return redirect('main_page')
        else:
            for error in form.errors:
                messages.error(request, form.errors[error].as_text())
            return redirect('registration')
    else:
        form = RegisterForm()
        context = {
            'title': 'Registration',
            'form': form
        }
        return render(request, 'registration.html', context)
