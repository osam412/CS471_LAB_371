from django.urls import path
from . import views

urlpatterns = [
 path('', views.index, name= "books.index"),
 path('list_books/', views.list_books, name= "books.list_books"),
 path('<int:bookId>/', views.viewbook, name="books.view_one_book"),
 path('aboutus/', views.aboutus, name="books.aboutus"), 


path('html5/links/', views.links, name="books.bookshtml"),
path('html5/text/formatting', views.formatters, name="books.formatters"), 
path('html5/listing', views.listing, name="books.listing"),
path('html5/tables', views.table, name="books.tables"),
path('search', views.Searching, name="books.search"),

path('simple/query', views.simple_query, name='simple_query'),

path('complex/query', views.complex_query, name='complex_query'),

path('lab8/task1', views.task1_view, name='task1'),
path('lab8/task2', views.task2_view, name='task2'),
path('lab8/task3', views.task3_view, name='task3'),
path('lab8/task4', views.task4_view, name='task4'),
path('lab8/task5', views.task5_view, name='task5'),
path('lab8/task7', views.task7_view, name='task7'),


]
