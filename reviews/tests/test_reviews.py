from books.models import Books
from reviews.models import Review
from django.contrib.auth import get_user_model
import pytest


@pytest.mark.django_db
def test_add_review(api_client, authenticate_user):
    user = authenticate_user

    book = Books.objects.create(title="Book 1", author="Author 1", genre="Adventure")

    response = api_client.post('/api/review/add', {'book_id': book.id, 'rating': 5}, format='json')

    assert response.status_code == 201
    assert response.data['book'] == book.id
    assert response.data['rating'] == 5

@pytest.mark.django_db
def test_update_review(api_client, authenticate_user):
    user = authenticate_user

    # Create a book and a review
    book = Books.objects.create(title="Book 1", author="Author 1", genre="Adventure")
    review = Review.objects.create(user=user, book=book, rating=4)

    response = api_client.post('/api/review/update', {'review_id': review.id, 'rating': 5}, format='json')

    assert response.status_code == 200
    assert response.data['rating'] == 5


@pytest.mark.django_db
def test_delete_review(api_client, authenticate_user):
    user = authenticate_user

    book = Books.objects.create(title="Book 1", author="Author 1", genre="Adventure")
    review = Review.objects.create(user=user, book=book, rating=4)

    response = api_client.post('/api/review/delete', {'review_id': review.id}, format='json')

    assert response.status_code == 204
    assert Review.objects.filter(id=review.id).count() == 0


@pytest.mark.django_db
def test_suggest_books(api_client, authenticate_user):
    user = authenticate_user

    book1 = Books.objects.create(title="Book 1", author="Author 1", genre="Adventure")
    book2 = Books.objects.create(title="Book 2", author="Author 2", genre="Adventure")
    book3 = Books.objects.create(title="Book 3", author="Author 3", genre="Mystery")


    Review.objects.create(user=user, book=book1, rating=5)

    response = api_client.get('/api/book/suggest/')

    assert response.status_code == 200
    assert len(response.data) > 0