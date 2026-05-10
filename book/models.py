from django.db import models

class Book(models.Model):
    class CoverChoices(models.TextChoices):
        HARD = "Hard", "Hardcover"
        SOFT = "SOFT", "Softcover"

    author = models.CharField(max_length=100)
    year_of_the_book = models.IntegerField(null=True, blank=True)
    title = models.CharField(max_length=255, null=True, blank=True)

    cover = models.CharField(
        max_length=4,
        choices=CoverChoices.choices,
        default=CoverChoices.HARD
        )

    inventory = models.PositiveIntegerField(default=0)

