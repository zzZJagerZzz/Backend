from django.db import models

# Create your models here.


class MyFirstModel (models.Model):
  MyFirstField = models.CharField(max_length=255)

  def __str__(self) -> str:
    return 'Название'