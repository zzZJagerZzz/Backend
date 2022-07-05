from django.db import models

# Create your models here.


class Person (models.Model):
    first_name = models.CharField(max_length=255, verbose_name='Имя')
    last_name = models.CharField(max_length=255, verbose_name='Фамилия')

    class Meta:
        ordering = ['first_name', 'last_name']
        unique_together = ['first_name', 'last_name']
        verbose_name = 'man'
        verbose_name_plural = 'people'

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Pet (models.Model):
    name = models.CharField(max_length=64, verbose_name='Имя')
    owner = models.ForeignKey(
        Person, verbose_name='Хозяин', on_delete=models.CASCADE, related_name='pets')

    class Meta:
        ordering = ['owner']
        unique_together = ['name', 'owner']
        verbose_name = 'pet'
        verbose_name_plural = 'pets'

    def __str__(self):
        return self.name
