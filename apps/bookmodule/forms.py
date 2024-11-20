from django import forms
from .models import Book
from apps.bookmodule import models


class BookForm(forms.ModelForm):
 class Meta: 
  model = models.Book # tell form that model to map
  fields = ['title', 'price', 'edition', 'author'] # tell form what to map from model

class DeleteBookForm(forms.Form):
    confirm = forms.BooleanField(required=True, label="Confirm Deletion")
   
