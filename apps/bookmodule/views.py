from django.shortcuts import get_object_or_404, render, redirect # type: ignore
from .models import Book, Gallery, Student, Student2
from django.db.models import Q
from django.db.models import Count, Sum, Avg, Max, Min
from .models import Address
from django.db.models import Count
from .forms import AddressForm, BookForm, DeleteBookForm, GalleryForm, Student2Form, StudentForm




#lab12
# Task 1
def task1(request):
    return render(request, 'bookmodule_2/lab12_task1.html')

# Task 2
def task2(request):
    return render(request, 'bookmodule_2/lab12_task2.html')

# Task 3
def task3(request):
    return render(request, 'bookmodule_2/lab12_task3.html')

# Task 4
def task4(request):
    return render(request, 'bookmodule_2/lab12_task4.html')

# Task 5
def task5(request):
    return render(request, 'bookmodule_2/lab12_task5.html')
#lab12

#lab7
def simple_query(request):
    mybooks=Book.objects.filter(title__icontains='and') # <- multiple objects
    return render(request, 'bookmodule/bookList.html', {'books':mybooks})

def complex_query(request):
    mybooks=books=Book.objects.filter(author__isnull =
False).filter(title__icontains='and').filter(edition__gte = 2).exclude(price__lte = 100)[:10]
    if len(mybooks)>=1:
        return render(request, 'bookmodule/bookList.html', {'books':mybooks})
    else:
        return render(request, 'bookmodule/index.html')
#lab7

#lab8
def task1_view(request):
     books = Book.objects.filter(Q(price__lte=50))
     return render(request, 'bookmodule/task1.html', {'books': books})

def task2_view(request):
    books = Book.objects.filter(Q(edition__gt=2) & (Q(title__icontains='qu') | Q(author__icontains='qu')))
    return render(request, 'bookmodule/task2.html', {'books': books})

def task3_view(request):
    books = Book.objects.filter(~Q(edition__gt=2) & ~Q(title__icontains='qu') & ~Q(author__icontains='qu'))
    return render(request, 'bookmodule/task3.html', {'books': books})

def task4_view(request):
    books = Book.objects.all().order_by('title')
    return render(request, 'bookmodule/task4.html', {'books': books})

def task5_view(request):
    stats = Book.objects.aggregate(
        total_books=Count('id'),
        total_price=Sum('price'),
        average_price=Avg('price'),
        max_price=Max('price'),
        min_price=Min('price')
    )
    return render(request, 'bookmodule/task5.html', {'stats': stats})


def task7_view(request):
    student_count_by_city = Address.objects.annotate(student_count=Count('student'))
    return render(request, 'bookmodule/task7.html', {'student_count_by_city': student_count_by_city})

#lab8

#lab9 
def listBooks_part1(request):
    books = Book.objects.all()  
    return render(request, 'bookmodule/lab9_part1_listbooks.html', {'books': books})
# Add Book
def addbook(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        price = float(request.POST.get('price', 0.0))
        edition = int(request.POST.get('edition', 1))
        
        Book.objects.create(title=title, author=author, price=price, edition=edition)
        return redirect('listBooks_part1')  

    return render(request, 'bookmodule/addBook.html')

# Update Book 
def updateBook_part1(request, id):
    book = Book.objects.get(id=id)
    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.price = float(request.POST.get('price', 0.0))
        book.edition = int(request.POST.get('edition', 1))
        book.save()
        return redirect('listBooks_part1')

    return render(request, 'bookmodule/updateBook_part1.html', {'book': book})

# Delete Book
def delete_book_part1(request,id):
  obj = Book.objects.get(id = id)
  if request.method=='POST':
    obj.delete() 
    return redirect('listBooks_part1')
  return render(request, "bookmodule/deletebook.html", {'obj':obj})

# ---------------------------
# Part 2: CRUD Operations With Forms
# ---------------------------

# Add Book Using Form

def addBook_part2(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listBooks_part2')
    else:
        form = BookForm(None)
    return render(request, 'bookmodule/addBook_part2.html', {'form': form})

# Update Book Using Form 
def updateBook_part2(request, id):
    book = Book.objects.get(id=id)
    form = BookForm(instance=book) 

    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save() 
            return redirect('listBooks_part2')  

    return render(request, 'bookmodule/updateBook_part2.html', {'form': form})

# Delete Book Using Form 
def delete_book_part2(request, id):
    obj = Book.objects.get(id=id)
    if request.method == 'POST':
        obj.delete()  
        return redirect('listBooks_part2')
    
    form = DeleteBookForm()  
    return render(request, 'bookmodule/deleteBook2.html', {'obj': obj, 'form': form})

def listBooks_part2(request):
    books = Book.objects.all() 
    return render(request, 'bookmodule/lab9_part2_listbooks.html', {'books': books})
#lab9

#lab10
# List Students
def list_students(request):
    students = Student.objects.select_related('address').all()
    return render(request, 'student/list_students.html', {'students': students})

# Add Student
def add_student(request):
    if request.method == 'POST':
        student_form = StudentForm(request.POST)
        address_form = AddressForm(request.POST)

        if student_form.is_valid() and address_form.is_valid():
            address = address_form.save()  # Save address first
            student = student_form.save(commit=False)  # Save student without committing to the database
            student.address = address  # Assign the newly saved address to student
            student.save()  # Save student to the database

            return redirect('list_students')
    else:
        student_form = StudentForm()
        address_form = AddressForm()

    return render(request, 'student/add_student.html', {'student_form': student_form, 'address_form': address_form})

# Update Student

def update_student(request, id):
    student = Student.objects.get(id=id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)  # Bind form with student data
        if form.is_valid():
            form.save()
            return redirect('list_students')
    else:
        form = StudentForm(instance=student)  # Prepopulate form with the student instance
    return render(request, 'student/update_student.html', {'form': form})

# Delete Student
def delete_student(request, id):
    student = Student.objects.get(id=id)
    if request.method == 'POST':
        student.delete()
        return redirect('list_students')
    return render(request, 'student/delete_student.html', {'student': student})



#task2
# Add/Update Student with Many-to-Many Relationship

def list_students2(request):
    students = Student2.objects.prefetch_related('addresses').all()
    return render(request, 'student/list_students2.html', {'students': students})

def add_student2(request):
    if request.method == 'POST':
        form = Student2Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_students2')
    else:
        form = Student2Form()
    return render(request, 'student/add_student2.html', {'form': form})

def update_student2(request, id):
    student = Student2.objects.get(id=id)
    if request.method == 'POST':
        form = Student2Form(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('list_students2')
    else:
        form = Student2Form(instance=student)

    return render(request, 'student/update_student2.html', {'form': form})

def delete_student2(request, id):
    student = Student2.objects.get(id=id)
    if request.method == 'POST':
        student.delete()
        return redirect('list_students2')
    return render(request, 'student/delete_student2.html', {'student': student})
#task2

# Add Image
def add_image(request):
    if request.method == 'POST':
        form = GalleryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list_images')
    else:
        form = GalleryForm()
    return render(request, 'bookmodule/add_image.html', {'form': form})

# List Images
def list_images(request):
    images = Gallery.objects.all()
    return render(request, 'gallery/list_images.html', {'images': images})

def update_image(request, id):
    gallery_item =  Gallery.objects.get(id=id)
    if request.method == 'POST':
        form = GalleryForm(request.POST, request.FILES, instance=gallery_item)
        if form.is_valid():
            form.save()
            return redirect('list_images')
    else:
        form = GalleryForm(instance=gallery_item)
    return render(request, 'gallery/update_image.html', {'form': form})

def delete_image(request, id):
    gallery_item = Gallery.objects.get(id=id)
    if request.method == 'POST':
        gallery_item.delete()
        return redirect('list_images')
    return render(request, 'gallery/delete_image.html', {'gallery_item': gallery_item})



#lab10
 
 
def index(request):
   return render(request, "bookmodule/index.html")
def list_books(request):
   return render(request, 'bookmodule/list_books.html')
def viewbook(request, bookId):
   return render(request, 'bookmodule/one_book.html')

def aboutus(request):
   return render(request, 'bookmodule/aboutus.html')

def links(request):
   return render(request, 'bookmodule/links.html')

def formatters(request):
   return render(request, 'bookmodule/format.html')
def listing(request):
   return render(request, 'bookmodule/listing.html')
def table(request):
   return render(request, 'bookmodule/tables.html')



def __getBooksList():
 book1 = {'id':12344321, 'title':'Continuous Delivery', 'author':'J.Humble and D. Farley'}
 book2 = {'id':56788765,'title':'Reversing: Secrets of Reverse Engineering', 'author':'E. Eilam'}
 book3 = {'id':43211234, 'title':'The Hundred-Page Machine Learning Book', 'author':'Andriy Burkov'}
 return [book1, book2, book3]

def Searching(request):
   if request.method == "POST":
     string = request.POST.get('keyword').lower()
     isTitle = request.POST.get('option1')
     isAuthor = request.POST.get('option2')
     # now filter
     books = __getBooksList()
     newBooks = []
     for item in books:
       contained = False
       if isTitle and string in item['title'].lower(): contained = True
       if not contained and isAuthor and string in item['author'].lower():contained = True

     if contained: 
        newBooks.append(item)

     return render(request, 'bookmodule/bookList.html', {'books':newBooks})
   return render(request, 'bookmodule/search.html')
 





def index2(request, val1 = 0): 
   return render("value1 = "+str(val1))

def viewbook(request, bookId):
     # assume that we have the following books somewhere (e.g. database)
     book1 = {'id':123, 'title':'Continuous Delivery', 'author':'J. Humble and D. Farley'}
     book2 = {'id':456, 'title':'Secrets of Reverse Engineering', 'author':'E. Eilam'}
     targetBook = None
     if book1['id'] == bookId: targetBook = book1
     if book2['id'] == bookId: targetBook = book2
     context = {'book':targetBook} # book is the variable name accessible by the template
     return render(request, 'bookmodule/show.html', context)
