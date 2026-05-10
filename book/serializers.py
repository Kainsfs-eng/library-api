from rest_framework import serializers
from .models import Book

class BookSerializer (serializers.ModelSerializer):
    covers_display = serializers.CharField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True)
    class Meta:
        model = Book
        fields = [
            'author',
            'year_of_the_book',
            'title','cover',
            'id',
            'covers_display',
        ]