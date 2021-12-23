from django.urls import path, include
from users.views import Login
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('login/', Login.as_view(), name='custom_login'),
    path('accounts/', include('django.contrib.auth.urls')),
]


urlpatterns += staticfiles_urlpatterns()
