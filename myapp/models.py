from django.db import models
from django.urls import reverse


class Menu(models.Model):
    name = models.CharField(
        max_length=80, )

    def get_absolute_url(self):
        return reverse('menu', kwargs={'menu_id': self.pk})

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    menu = models.ForeignKey(
        Menu,
        verbose_name='menu',
        null=True,
        on_delete=models.SET_NULL,
    )

    name = models.CharField(
        max_length=150,
    )
    uri = models.SlugField(
        blank=True,
        null=True,
    )

    def get_absolute_url(self):
        return reverse('item', kwargs={'item_id': self.pk})

    def __str__(self):
        return self.name
