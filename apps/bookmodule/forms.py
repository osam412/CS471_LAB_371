from django import forms
from .models import Book, Gallery
from apps.bookmodule import models
from .models import Student, Address
from .models import Student2, Address2
from . import models

class BookForm(forms.ModelForm):
 class Meta: 
  model = models.Book # tell form that model to map
  fields = ['title', 'price', 'edition', 'author'] # tell form what to map from model

class DeleteBookForm(forms.Form):
    confirm = forms.BooleanField(required=True, label="Confirm Deletion")

#lab10
class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['city']

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age', 'address']


#task2
class Address2Form(forms.ModelForm):
    class Meta:
        model = Address2
        fields = ['city']

class Student2Form(forms.ModelForm):
    class Meta:
        model = Student2
        fields = ['name', 'age', 'addresses']
#task2

 #task3       
class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = ['image', 'description']   
        
#lab10