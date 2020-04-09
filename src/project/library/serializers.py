from rest_framework import serializers

from library.models import Writer, Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["id", "name"]


class WritersBooksSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Writer
        fields = ["id", "name", "books"]
