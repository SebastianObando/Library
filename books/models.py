from authors.models import Author
from django.db import models

# Create your models here.

class Book(models.Model):
  title = models.CharField(max_length=250)
  release_date =  models.DateField()
  isbn = models.CharField(max_length=100)
  description = models.CharField(max_length=500)
  price = models.IntegerField()
  stock = models.IntegerField()
  publisher = models.CharField(max_length=30)
  picture = models.ImageField(upload_to='books/pics', blank=True)

  authors = models.ManyToManyField(Author)

  def __str__(self):
      return self.title
  