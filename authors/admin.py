from books import models
from django.contrib import admin
from authors.models import Author

# Register your models here.
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
  list_display = ('pk', 'name', 'last_name', 'nick_name', 'birth_date')
