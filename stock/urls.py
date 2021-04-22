from django.urls import path
from .views import StockView, BookView, AuthorView, BookByAuthorView, CountBookByStockView, BookToStockView

app_name = "stock"

urlpatterns = [
    path('stock/', StockView.as_view()),
    path('book/', BookView.as_view()),
    path('book/<int:book>', BookView.as_view()),
    path('book-by-author/<int:author>', BookByAuthorView.as_view(),),
    path('count-book-by-stock/<int:stock>', CountBookByStockView.as_view(),),
    path('quantity/', BookToStockView.as_view(),),
    path('quantity/<int:book>/<int:stock>', BookToStockView.as_view(),),
    path('author/', AuthorView.as_view()),
    path('author/<int:author>', AuthorView.as_view()),
]