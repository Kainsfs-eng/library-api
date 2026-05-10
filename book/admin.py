from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "year_of_the_book", "inventory", "cover")
    list_display_links = ("title",)
    list_filter = ("cover", "author")
    search_fields = ("title", "author")
    list_editable = ("inventory",)