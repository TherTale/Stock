from django.contrib import admin
from .models import Book, Author, City, Stocks, Quantity

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(City)
admin.site.register(Stocks)
admin.site.register(Quantity)
