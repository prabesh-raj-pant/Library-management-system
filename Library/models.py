from django.db import models

# Create your models here.
class Book(models.Model): 
    Title=models.CharField(max_length=200)
    ISBN=models.IntegerField(primary_key=True)
    Publisher=models.CharField(max_length=200)
    Year=models.DateField()
    Genere=models.CharField(max_length=200)
    
    
class Member(models.Model): 
    Name=models.CharField(max_length=100)
    Address=models.CharField(max_length=100)
    Email=models.EmailField(unique=True)
    Phone=models. FloatField(max_length=10)

class Loan(models.Model): 
    Book_id=models.ForeignKey(Book, on_delete=models.CASCADE,related_name="loans")
    Memberr_id=models.ForeignKey(Member,on_delete=models.CASCADE,related_name="loans")
    Loan_date=models.DateTimeField()
    Return_date=models.DateTimeField(null=True,blank=True)

class Author(models.Model): 
    Name=models.CharField(max_length=100)
    Bio=models.CharField(max_length=600)


class Librarian(models.Model): 
    Name=models.CharField(max_length=100)
    Employee_id=models.IntegerField(unique=True)
    Email=models.EmailField(unique=True)
    
