from rest_framework import serializers
from app.models import Book, Author

class BookSerializer(serializers.ModelSerializer):

    class Meta:

        model = Book
        fields = (
            'id',
            'name',
            'description',
            'author',
        )

class AuthorSerializer(serializers.ModelSerializer):

    class Meta:

        model = Author
        fields = (
            'id',
            'name',
        )