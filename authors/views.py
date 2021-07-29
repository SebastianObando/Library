import authors
from django.shortcuts import render
from django.views.generic import DetailView, ListView
from authors.models import Author
from books.models import Book

# Create your views here.
class AuthorBooksView(DetailView):
  template_name = 'books_by_author.html'
  slug_field = 'pk'
  slug_url_kwarg = 'pk'
  queryset = Author.objects.all()
  context_object_name = 'author'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    author = self.get_object()
    context.update({'books' : Book.objects.filter(authors=author).order_by('release_date')})
    return context

class AllAuthors(ListView):
  template_name = 'authors.html'
  model = Author
  ordering = ('-created')
  context_object_name = 'authors'