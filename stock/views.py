from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404

from .models import Stocks,City, Book, Author, Quantity
from .serializers import StockSerializer, BookSerializer, AuthorSerializer, QuantitySerializer

class StockView(APIView):
    def get(self, request):
        stocks = Stocks.objects.all()
        serializer = StockSerializer(stocks, many=True)
        return Response({"Склады": serializer.data})
    
    def post(self,request):
        stock = request.data.get('stocks')
        serializer = StockSerializer(data=stock)
        if serializer.is_valid(raise_exception=True):
            stock_saved = serializer.save()
        return Response({
            "success": "Stock '{}' created successfully".format(stock_saved.title)
            })
    
    
class BookView(APIView):
    def get(self, request):
        book = Book.objects.all()
        serializer = BookSerializer(book, many=True)
        return Response({"Книги": serializer.data})
    
    def post(self,request):
        book = request.data.get('book')
        serializer = BookSerializer(data=book)
        if serializer.is_valid(raise_exception=True):
            author_saved = serializer.save()
        return Response({
            "success": "Book '{}' created successfully".format(author_saved.title)
            })
        
    def put(self,request,book):
        saved_book = get_object_or_404(Book.objects.all(), pk=book)
        data = request.data.get('book')
        serializer = BookSerializer(instance=saved_book, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            saved_book = serializer.save()
        return Response({
            "success": "Book '{}' updated successfully".format(saved_book.title)
        })
        
    def delete(self, request, book):
        book = get_object_or_404(Book.objects.filter(id=book))
        book.delete()
        return Response({
            "message": "Book with id `{}` has been deleted.".format(author)
        }, status=204)
    
    
class AuthorView(APIView):
    def get(self, request):
        author = Author.objects.all()
        serializer = AuthorSerializer(author, many=True)
        return Response({"Авторы": serializer.data})
    
    def post(self,request):
        author = request.data.get('author')
        serializer = AuthorSerializer(data=author)
        if serializer.is_valid(raise_exception=True):
            author_saved = serializer.save()
        return Response({
            "success": "Author '{}' created successfully".format(author_saved.second_name+" "+author_saved.first_name)
            })
        
    def put(self,request,author):
        saved_author = get_object_or_404(Author.objects.all(), pk=author)
        data = request.data.get('author')
        serializer = AuthorSerializer(instance=saved_author, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            saved_author = serializer.save()
        return Response({
            "success": "Author '{}' updated successfully".format(saved_author.first_name)
        })
        
    def delete(self, request, author):
        author = get_object_or_404(Author.objects.filter(id=author))
        author.delete()
        return Response({
            "message": "Author with id `{}` has been deleted.".format(author)
        }, status=204)
    
    
class BookByAuthorView(APIView):
    def get(self,request, author):
        book = Book.objects.filter(author__id__icontains=author)
        serializer = BookSerializer(book, many=True)
        return Response({"Книги": serializer.data})
    
class CountBookByStockView(APIView):
    def get(self,request, stock):
        stocks = Quantity.objects.filter(id=stock)
        count=0
        for books in stocks:
            count += books.count
        return Response({"Книг на складе": count})
    
class BookToStockView(APIView):
    def get(self, request):
        quantity = Quantity.objects.all()
        serializer = QuantitySerializer(quantity, many=True)
        return Response({"Книги на складах": serializer.data})
    
    def post(self,request):
        quantity = request.data.get('quantity')
        serializer = QuantitySerializer(data=quantity)
        if serializer.is_valid(raise_exception=True):
            quantity_saved = serializer.save()
        return Response({
            "success": "Records created successfully"
            })
        
    def put(self,request,book,stock):
        saved_count_books = get_object_or_404(Quantity.objects.filter(book_id=book, stock_id=stock))
        data = request.data.get('quantity')
        serializer = QuantitySerializer(instance=saved_count_books, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            saved_count_books = serializer.save()
        return Response({
            "success": "Count record updated successfully"
        })