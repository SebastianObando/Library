from django.db import models
from django.db.models.fields import CharField


# Create your models here.

class Author(models.Model):
  name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)
  nick_name = models.CharField(max_length=30)
  birth_date = models.DateField()

  created = models.DateTimeField(auto_now_add=True)
  modified = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.name + self.last_name
  