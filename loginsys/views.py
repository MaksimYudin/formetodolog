# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect
from django.contrib import auth
from django.template.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm
from .forms import ProfileForm, UserCreateForm, SignupForm
from .models import User
from datetime import datetime
import account.views

def login(request):
    context = {}
    context.update(csrf(request))
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            context['login_error'] = 'Пользователь не найден'
            return render_to_response('login.html', context)
    else:
        return render_to_response('login.html', context)

def logout(request):
    auth.logout(request)
    return redirect('/')

def register(request):
    context = {
        'user_form':UserCreateForm,
        'profile_form':ProfileForm,
        'date_test':format(datetime.today().date(), '%d-%m-%Y')
    }
    context.update(csrf(request))
    if request.POST:
        newuser_form = UserCreateForm(request.POST)
        #profile_form = ProfileForm(request.POST)
        if newuser_form.is_valid():
            newuser_form.save()
            newuser = auth.authenticate(username=newuser_form.cleaned_data['username'], password=newuser_form.cleaned_data['password2'])
            auth.login(request, newuser)
            return redirect('/')
        else:
            context['form'] = newuser_form
            print(newuser_form.errors)
    return render_to_response('register.html', context)

class SignupView(account.views.SignupView):

    form_class = SignupForm
    identifier_field = 'email'

    def after_signup(self, form):
        self.create_profile(form)
        super(SignupView, self).after_signup(form)

    def create_profile(self, form):
        profile = self.created_user.profile  # replace with your reverse one-to-one profile attribute
        profile.birth_date = form.cleaned_data["birthdate"]
        profile.location = form.cleaned_data["location"]
        profile.save()

    def generate_username(self, form):
        # do something to generate a unique username (required by the
        # Django User model, unfortunately)
        username = form.cleaned_data["email"]
        return username

class LoginView(account.views.LoginView):

    form_class = account.forms.LoginEmailForm