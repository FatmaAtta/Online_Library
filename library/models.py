from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    confirm_password = models.CharField(max_length=100)
    is_admin = models.BooleanField(default=False)
    def __str__(self):
        return self.username

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    is_available = models.BooleanField(default=True)
    is_borrowed = models.BooleanField(default=False)
    description = models.TextField()
    cover_page = models.ImageField(upload_to='img/')
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.name
