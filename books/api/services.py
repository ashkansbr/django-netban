from django.core.exceptions import ValidationError
from ..models import Book


def create_book(title, author, genre):

    if Book.objects.filter(title=title, author=author).exists():
        raise ValidationError("A book with this title and author already exists.")

    book = Book.objects.create(title=title, author=author, genre=genre)
    return book


def update_book(book_id, title=None, author=None, genre=None):
    try:
        book = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        raise ValidationError("Book does not exist.")

    if title:
        book.title = title
    if author:
        book.author = author
    if genre:
        book.genre = genre

    book.save()
    return book


def delete_book(book_id):
    try:
        book = Book.objects.get(id=book_id)
        book.delete()
        return True
    except Book.DoesNotExist:
        raise ValidationError("Book does not exist.")
