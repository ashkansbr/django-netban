from ..models import Review

def get_reviews_by_user(user):
    return Review.objects.filter(user=user)
