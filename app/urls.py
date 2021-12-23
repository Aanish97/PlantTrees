from django.urls import path

from app.views import HomeView
from users.views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
]

urlpatterns += staticfiles_urlpatterns()
