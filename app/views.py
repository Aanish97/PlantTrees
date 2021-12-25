from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from django.core.files.storage import default_storage

from app.models import Plant
from app.serializers import PlantsSerializer


class CreatePostView(TemplateView, LoginRequiredMixin):
    template_name = "create_post.html"
    login_url = '/users/login/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def post(self, request):
        area = request.POST.get('area')
        description = request.POST.get('description')
        file = request.FILES.get('file')

        file_name = ''
        if file:
            file_name = default_storage.save(f"{file.name}", file)

        Plant.objects.create(user=request.user, area=area, description=description,
                             file=file.name if file_name else '')

        plants = PlantsSerializer(Plant.objects.all().order_by('-created_at'), many=True).data
        return render(request, "home.html", {"plants": plants})


class HomeView(TemplateView, LoginRequiredMixin, View):
    template_name = "home.html"
    login_url = '/users/login/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['plants'] = PlantsSerializer(Plant.objects.all().order_by('-created_at'), many=True).data
        return context
