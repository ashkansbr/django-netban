import pytest
from books.api.services import create_book
from django.core.exceptions import ValidationError

@pytest.mark.django_db
def test_create_book_success():
    book = create_book("New Book", "New Author", "Adventure")
    assert book.title == "New Book"
    assert book.author == "New Author"
    assert book.genre == "Adventure"

@pytest.mark.django_db
def test_create_book_duplicate():
    create_book("Test Book", "Test Author", "Fiction")
    with pytest.raises(ValidationError, match="A book with this title and author already exists."):
        create_book("Test Book", "Test Author", "Fiction")