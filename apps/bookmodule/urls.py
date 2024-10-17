from django.urls import path
from . import views

urlpatterns = [
 path('', views.index, name= "books.index"),
 path('list_books/', views.list_books, name= "books.list_books"),
 path('<int:bookId>/', views.viewbook, name="books.view_one_book"),
 path('aboutus/', views.aboutus, name="books.aboutus"), 
 path('/', views.aboutus, name="books.aboutus"), 

path('html5/links/', views.links, name="books.bookshtml"),
path('html5/text/formatting', views.formatters, name="books.formatters"), 
path('html5/listing', views.listing, name="books.listing"),
path('html5/tables', views.table, name="books.tables"),



]
