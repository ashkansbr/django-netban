from django.db import models
from common.basemodel import BaseModel

class Books(BaseModel):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    genre = models.CharField(max_length=50)

    class Meta:
        unique_together = ('title', 'author', 'genre')

    def __str__(self):
        return self.title
