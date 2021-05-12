from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from book.models import Book


class BookSerializer(serializers.Serializer):
    book_name = serializers.CharField(max_length=50)
    author = serializers.CharField(max_length=75)
    price = serializers.IntegerField()

    def create(self, validated_data):
        return Book.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.book_name = validated_data.get("book_name")
        instance.author = validated_data.get("author")
        instance.price = validated_data.get("price")
        instance.save()
        return instance


class BookModelSerializar(ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'



class LoginSerializer(serializers.Serializer):
    username=serializers.CharField()
    password=serializers.CharField()