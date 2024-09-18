from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.exceptions import ValidationError
from rest_framework import status
from .serializers import BookSerializer
from .selectors import get_books_by_genre, get_all_books
from .services import create_book


class BookViewSet(viewsets.ViewSet):

    def list(self, request):
        books = get_all_books()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def create(self, request):
        title = request.data.get('title')
        author = request.data.get('author')
        genre = request.data.get('genre')

        try:
            book = create_book(title, author, genre)
            return Response(BookSerializer(book).data, status=status.HTTP_201_CREATED)
        except ValidationError as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class BookRecommendationAPIView(APIView):

    def get(self, request):
        genre = request.query_params.get('genre')
        if genre:
            books = get_books_by_genre(genre)
            serializer = BookSerializer(books, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"detail": "Genre not provided"}, status=status.HTTP_400_BAD_REQUEST)
