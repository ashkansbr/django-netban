from django.db import transaction
from django.core.exceptions import ValidationError
from ..models import Review
from books.models import Books


@transaction.atomic
def create_review(user, book_id, rating):
    if not (1 <= rating <= 5):
        raise ValidationError("Rating must be between 1 and 5.")

    book = Books.objects.get(id=book_id)
    review, created = Review.objects.get_or_create(user=user, book=book, defaults={'rating': rating})

    if not created:
        review.rating = rating
        review.save()

    return review


@transaction.atomic
def update_review(user, review_id, rating):
    review = Review.objects.get(id=review_id, user=user)
    if not (1 <= rating <= 5):
        raise ValidationError("Rating must be between 1 and 5.")

    review.rating = rating
    review.save()
    return review


@transaction.atomic
def delete_review(user, review_id):
    review = Review.objects.get(id=review_id, user=user)
    review.delete()
