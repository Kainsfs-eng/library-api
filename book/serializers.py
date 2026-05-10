from rest_framework import serializers
from .models import Book

class BookSerializer (serializers.ModelSerializer):
    covers_display = serializers.CharField(read_only=True)
    class Meta:
        model = Book
    class Meta:
        model = Book
        filter = [
            'author','year_of_the_book','title','cover',
        ]