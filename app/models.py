from django.db import models
from django.db.models import CASCADE


class Plant(models.Model):
    user = models.ForeignKey('users.User', on_delete=CASCADE)
    title = models.CharField(max_length=255, verbose_name='title')
    description = models.CharField(max_length=255, verbose_name='description')
    file = models.FileField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
