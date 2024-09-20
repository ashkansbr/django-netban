from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import BookSerializer
from django.core.exceptions import ValidationError
from .selectors import get_all_books, get_books_by_genre
from .services import suggest_books_based_on_reviews


class BookListAPIView(APIView):
    def get(self, request):
        genre = request.query_params.get('genre')
        if genre:
            books = get_books_by_genre(genre)
        else:
            books = get_all_books()

        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class SuggestBooksAPIView(APIView):
    def get(self, request):
        user = request.user
        try:
            suggested_books = suggest_books_based_on_reviews(user)
            if not suggested_books:
                return Response({"detail": "there is not enough data about you"}, status=status.HTTP_404_NOT_FOUND)

            serializer = BookSerializer(suggested_books, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ValidationError as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)