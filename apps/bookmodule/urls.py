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

#lab9
path('lab9_part1/listbooks/', views.listBooks_part1, name='listBooks_part1'),
path('lab9_part1/addbook/', views.addbook, name='addbook'),
path('lab9_part1/editbook/<int:id>/', views.updateBook_part1, name='updateBook_part1'),
path('lab9_part1/deletebook/<int:id>/', views.delete_book_part1, name='delete_book_part1'),
path('lab9_part2/addbook', views.addBook_part2, name='addBook_part2'),
path('lab9_part2/editbook/<int:id>/', views.updateBook_part2, name='updateBook_part2'),
path('lab9_part2/deletebook/<int:id>/', views.delete_book_part2, name='delete_book_part2'),
path('lab9_part2/listbooks/', views.listBooks_part2, name='listBooks_part2'),
#lab9

#lab10
path('students/', views.list_students, name='list_students'),
path('students/add/', views.add_student, name='add_student'),
path('students/update/<int:id>/', views.update_student, name='update_student'),
path('students/delete/<int:id>/', views.delete_student, name='delete_student'),

path('students2/', views.list_students2, name='list_students2'),
path('students2/add/', views.add_student2, name='add_student2'),
path('students2/update/<int:id>/', views.update_student2, name='update_student2'),
path('students2/delete/<int:id>/', views.delete_student2, name='delete_student2'),

#books/students2/delete/1/
# Gallery CRUD URL patterns
    path('gallery/', views.list_images, name='list_images'),
    path('gallery/add/', views.add_image, name='add_image'),
    path('gallery/update/<int:id>/', views.update_image, name='update_image'),
    path('gallery/delete/<int:id>/', views.delete_image, name='delete_image'),
#lab10



]
