from ..models import Book

def get_books_by_genre(genre):
    return Book.objects.filter(genre=genre)

def get_all_books():
    return Book.objects.all()