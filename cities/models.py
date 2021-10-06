from django.db import models
from django.urls import reverse


class City(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Город_name')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Город_Meta'
        verbose_name_plural = 'Города_Meta'

    def get_absolute_url(self):
        return reverse('cities:detail', kwargs={'pk': self.pk})
