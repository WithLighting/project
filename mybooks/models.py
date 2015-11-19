from django.db import models

# Create your models here.
class Author(models.Model):
    AuthorID = models.CharField(max_length=30,primary_key=True)
    Name = models.CharField(max_length=30)
    Age = models.CharField(max_length=30)
    Country = models.CharField(max_length=30)
class Book(models.Model):
    ISBN = models.CharField(max_length=30, primary_key = True)
    AuthorID = models.ForeignKey(Author)
    Title = models.CharField(max_length=30)
    Publisher = models.CharField(max_length=30)
    PublishDate = models.CharField(max_length=30)
    Price = models.CharField(max_length=15)	