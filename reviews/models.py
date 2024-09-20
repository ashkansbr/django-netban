from django.db import models
from django.contrib.auth import get_user_model
from books.models import Books

User = get_user_model()

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    rating = models.IntegerField()

    class Meta:
        unique_together = ('user', 'book')
        constraints = [
            models.CheckConstraint(check=models.Q(rating__gte=1, rating__lte=5), name='valid_rating'),
        ]

    def __str__(self):
        return f"{self.user} rated {self.book} {self.rating}/5"
