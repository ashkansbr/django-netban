from django.urls import path
from .views import AddReviewAPIView, UpdateReviewAPIView, DeleteReviewAPIView

urlpatterns = [
    path('review/add', AddReviewAPIView.as_view(), name='add-review'),
    path('review/update', UpdateReviewAPIView.as_view(), name='update-review'),
    path('review/delete', DeleteReviewAPIView.as_view(), name='delete-review'),
]
