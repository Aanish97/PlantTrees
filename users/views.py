from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.views import View


class Login(LoginView):
    login_url = '/login/'
    redirect_field_name = '/home/'
