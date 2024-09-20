from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ReviewSerializer
from django.core.exceptions import ValidationError
from .services import create_review, update_review, delete_review


class AddReviewAPIView(APIView):
    def post(self, request):
        user = request.user
        book_id = request.data.get('book_id')
        rating = request.data.get('rating')

        try:
            review = create_review(user, book_id, rating)
            return Response(ReviewSerializer(review).data, status=status.HTTP_201_CREATED)
        except ValidationError as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class UpdateReviewAPIView(APIView):
    def post(self, request):
        user = request.user
        review_id = request.data.get('review_id')
        rating = request.data.get('rating')

        try:
            review = update_review(user, review_id, rating)
            return Response(ReviewSerializer(review).data, status=status.HTTP_200_OK)
        except ValidationError as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class DeleteReviewAPIView(APIView):
    def post(self, request):
        user = request.user
        review_id = request.data.get('review_id')

        try:
            delete_review(user, review_id)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ValidationError as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)
