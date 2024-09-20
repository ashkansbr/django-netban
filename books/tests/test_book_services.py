import pytest
from books.models import Books


@pytest.mark.django_db
def test_list_all_books(api_client, authenticate_user):
    user = authenticate_user

    Books.objects.create(title="Book 1", author="Author 1", genre="Adventure")
    Books.objects.create(title="Book 2", author="Author 2", genre="Mystery")
    response = api_client.get('/api/book/list/?genre=Adventure')

    assert response.status_code == 200
    assert len(response.data) == 1
    assert response.data[0]['title'] == 'Book 1'

@pytest.mark.django_db
def test_filter_books_by_genre(api_client, authenticate_user):
    user = authenticate_user

    Books.objects.create(title="Book 1", author="Author 1", genre="Adventure")
    Books.objects.create(title="Book 2", author="Author 2", genre="Mystery")

    response = api_client.get('/api/book/list/?genre=Adventure')

    assert response.status_code == 200
    assert len(response.data) == 1
    assert response.data[0]['title'] == 'Book 1'
