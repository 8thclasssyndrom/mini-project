from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Card(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя доктора')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    number = PhoneNumberField(unique=True, null=False, blank=False, region='KG')
    image = models.ImageField(blank=True, null=True, upload_to='card')
    address = models.CharField(max_length=100, verbose_name='Адрес')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'cards'
        verbose_name = 'card'






