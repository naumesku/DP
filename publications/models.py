from datetime import datetime
from django.conf import settings
from django.db import models
from conf_my import NULLABLE
from django.contrib.auth import get_user_model


class Publication(models.Model):
    """Модель публикации"""
    title = models.CharField(max_length=250, verbose_name='название')
    body = models.TextField(verbose_name='содержимое')
    photo = models.ImageField(upload_to='publications/', verbose_name='фото', **NULLABLE)
    pub_date = models.DateField(default=datetime.now, verbose_name='дата публикации')
    is_pay = models.BooleanField(default=False, verbose_name='платная публикация')
    is_active = models.BooleanField(default=True, verbose_name='Активна')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE, verbose_name="автор публикации")

    def save(self, *args, **kwargs):
        if not self.author:
            self.author = get_user_model().objects.get(is_active=True)
        else:
            self.author = self.author
        super().save(*args, **kwargs)

    def __str__(self):
        return

    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'
