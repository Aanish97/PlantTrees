from django.urls import path

from app.views import HomeView, CreatePostView
from users.views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('home/', HomeView.as_view(), name='home'),
    path('create-post/', CreatePostView.as_view(), name='create-post'),
]

urlpatterns += staticfiles_urlpatterns()
