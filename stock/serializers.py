from rest_framework import serializers

from .models import Stocks, City, Book, Author,Quantity


class StockSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=50)
    city_id = serializers.IntegerField()

    def create(self, validated_data):
        return Stocks.objects.create(**validated_data)


class BookSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=20)
    author_id = serializers.IntegerField()
    cost = serializers.IntegerField()
    
    def create(self, validated_data):
        return Book.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.author_id = validated_data.get('author_id', instance.author_id)
        instance.cost = validated_data.get('cost', instance.cost)
        instance.save()
        return instance


class AuthorSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=50)
    second_name = serializers.CharField(max_length=50)
    
    def create(self, validated_data):
        return Author.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.second_name = validated_data.get('second_name', instance.second_name)
        instance.save()
        return instance
    
class QuantitySerializer(serializers.Serializer):
    book_id = serializers.IntegerField()
    stock_id = serializers.IntegerField()
    count = serializers.IntegerField()
    
    def create(self, validated_data):
        return Quantity.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.count = validated_data.get('count', instance.count)
        instance.save()
        return instance