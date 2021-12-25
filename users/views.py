from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from users.models import User


class Login(LoginView):
    login_url = '/users/login/'
    redirect_field_name = '/home/'


class Logout(LogoutView):
    next_page = '/users/login/'
    redirect_field_name = '/users/login/'


class Register(TemplateView):
    template_name = 'register.html'

    def get(self, request):
        return render(request, 'register.html', {})

    def post(self, request):

        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            try:
                try:
                    User.objects.get(email=email)
                    return render(request, self.template_name, {'errors': 'Email already exists.'})
                except User.DoesNotExist:
                    User.objects.create_user(username=username, password=password, email=email)
            except Exception as e:
                if str(e) == 'UNIQUE constraint failed: users_user.username':
                    return render(request, self.template_name, {'errors': 'Username already taken.'})
                return render(request, self.template_name, {'errors': e})
        else:
            return render(request, self.template_name, {'errors': 'Passwords do not match.'})

        return render(request, self.template_name, {'success': 'New User created'})
