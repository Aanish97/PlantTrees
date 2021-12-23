from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from rest_framework.decorators import permission_classes


class HomeView(TemplateView, LoginRequiredMixin, View):
    template_name = "home.html"
    login_url = '/users/login/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['name'] = 'data'
        return context
