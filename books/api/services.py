from django.db import models
from ..models import Books
from django.core.exceptions import ValidationError
from reviews.models import Review


def create_book(title, author, genre):
    if Books.objects.filter(title=title, author=author).exists():
        raise ValidationError("A book with this title and author already exists.")

    book = Books.objects.create(title=title, author=author, genre=genre)
    return book




def suggest_books_based_on_reviews(user):
    favorite_genre = (
        Review.objects.filter(user=user)
        .values('book__genre')
        .annotate(count=models.Count('book__genre'))
        .order_by('-count')
        .first()
    )

    if not favorite_genre:
        raise ValidationError("there is not enough data about you")

    genre = favorite_genre['book__genre']
    suggested_books = Books.objects.filter(genre=genre).exclude(review__user=user)
    return suggested_books