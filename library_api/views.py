from rest_framework import viewsets
from book.models import Book
from book.serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    """
     View set for Book model
     list,create,retrieve,update,partial_update,destroy.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer