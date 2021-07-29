from django.urls import path
from books import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path(route='', view=views.BooksAvaliablesView.as_view(), name='products'),
    path(route='book/<int:pk>', view=views.BookDetailView.as_view(), name='detail_book')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)