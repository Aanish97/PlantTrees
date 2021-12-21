from django.urls import path
from users.views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    # path('', HomeView.as_view(), name='balance'),
]

urlpatterns += staticfiles_urlpatterns()
