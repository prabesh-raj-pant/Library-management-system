from django.db import models

# Create your models here.
class Book(models.Model): 
    Title=models.CharField(max_length=200)
    ISBN=models.IntegerField(primary_key=True)
    Publisher=models.CharField(max_length=200)
    Year=models.DateField()
    Genere=models.CharField(max_length=200)
    
    def __str__(self) :
        return self.Title
    
    
class Member(models.Model): 
    Member_id=models.IntegerField(unique=True)
    Name=models.CharField(max_length=100)
    Address=models.CharField(max_length=100)
    Email=models.EmailField(unique=True)
    Phone=models. FloatField(max_length=10)
    
    def __str__(self):
        return self.Name

class Loan(models.Model): 
    Book_id=models.ForeignKey(Book, on_delete=models.CASCADE,related_name="loans")
    Memberr_id=models.ForeignKey(Member,on_delete=models.CASCADE,related_name="loans")
    Loan_date=models.DateTimeField(auto_now_add=True)
    Return_date=models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return f"{self.book.title} loaned by {self.member.name}"

class Author(models.Model): 
    Name=models.CharField(max_length=100)
    Bio=models.CharField(max_length=600)

    def __str__(self):
        return self.Name

class Librarian(models.Model): 
    Name=models.CharField(max_length=100)
    Employee_id=models.IntegerField(unique=True)
    Email=models.EmailField(unique=True)
    
