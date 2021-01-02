from django.db import models


# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=20)
    DoB = models.DateField()

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=20)
    author = models.ForeignKey(Author, default=1, on_delete=models.SET_DEFAULT)
    category = models.CharField(max_length=20)
    printer = models.CharField(max_length=20)
    description = models.TextField()
    release_date = models.DateField()

    def __str__(self):
        return self.name



