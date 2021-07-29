from django.views.generic import ListView, DetailView
from books.models import Book

# Create your views here.
class BooksAvaliablesView(ListView):
  template_name = 'books_library.html'
  model = Book
  ordering = ('price',)
  paginate_by = 30
  context_object_name = 'books'

class BookDetailView(DetailView):
  template_name = 'detail_book.html'
  queryset = Book.objects.all()
  context_object_name = 'book'
  