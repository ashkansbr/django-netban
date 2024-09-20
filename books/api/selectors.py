from ..models import Books

def get_all_books():
    """Retrieve all books"""
    return Books.objects.all()

def get_books_by_genre(genre):
    """Retrieve books by genre"""
    return Books.objects.filter(genre=genre)
