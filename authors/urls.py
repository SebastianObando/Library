from django.urls import path
from authors import views


urlpatterns = [
  path(route='', view=views.AllAuthors.as_view(), name='all_authors'),
  path(route='<int:pk>', view=views.AuthorBooksView.as_view(), name='books_by'),
]