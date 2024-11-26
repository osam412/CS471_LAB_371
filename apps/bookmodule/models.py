from django.db import models # type: ignore

# Create your models here.
class Book(models.Model):
     title = models.CharField(max_length = 50)
     author = models.CharField(max_length = 50)
     price = models.FloatField(default = 0.0)
     edition = models.SmallIntegerField(default = 1)
     
#task1
class Address(models.Model):
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.city

# Student Model
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.ForeignKey(Address, on_delete=models.CASCADE)  # Each student can have one address, but an address can be assigned to multiple students

    def __str__(self):
        return self.name
    

#task2
class Address2(models.Model):
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.city

class Student2(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    addresses = models.ManyToManyField(Address2)  # Many-to-Many relationship 
    def __str__(self):
        return self.name


class Gallery(models.Model):
    description = models.TextField()
    image = models.ImageField(upload_to='images/')