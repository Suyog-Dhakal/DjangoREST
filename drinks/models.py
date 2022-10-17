from unittest.util import _MAX_LENGTH
from django.db import models

class Drink(models.Model):
  name = models.CharField(max_length=200)
  decription = models.CharField(max_length=500)

  def __str__(self):
    return self.name + '->  '  + self.decription