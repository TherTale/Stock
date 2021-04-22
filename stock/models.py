from django.db import models
import uuid


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.CASCADE, null=True)
    cost = models.IntegerField()

    def __str__(self):
        return self.title


class Author(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)

    def __str__(self):
        return '%s %s' % (self.second_name, self.first_name)


class City(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Stocks(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    city = models.ForeignKey('City', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title


class Quantity(models.Model):
    book = models.ForeignKey('Book', on_delete=models.CASCADE, null=True)
    stock = models.ForeignKey('Stocks', on_delete=models.CASCADE, null=True)
    count = models.IntegerField()

    def __str__(self):
        return '%s -> %s' % ( self.book, self.stock)