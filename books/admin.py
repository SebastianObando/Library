from books.models import Book
from django.contrib import admin

# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
  list_display = ('pk', 'title', 'release_date', 'isbn', 'stock')