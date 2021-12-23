from django.db import models
from django.db.models import CASCADE


class Plant(models.Model):
    user = models.ForeignKey('users.User', on_delete=CASCADE)
    area = models.CharField(max_length=255, verbose_name='area')
    description = models.CharField(max_length=255, verbose_name='description')
    file = models.FileField(null=True, blank=True)
    stars = models.IntegerField(default=0)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.area}"
