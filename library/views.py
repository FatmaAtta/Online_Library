from django.shortcuts import render, redirect
from .models import User, Book, Category
def books(request):
    return render(request, 'library/books.html')

def borrowed(request):
    return render(request, 'library/borrowed.html')

def details(request):
    return render(request, 'library/bookdetails.html')

def base(request):
    return render(request, 'library/base.html')

def main(request):
    return render(request, 'library/main.html')

def signin(request):
    return render(request, 'library/signin.html')

def adminpage(request):
    return render(request, 'library/adminpage.html')

def signup(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        is_admin=request.POST.get('is_admin')
        if is_admin=="" or is_admin is None:
            is_admin=False
        else:
            is_admin=True
        user=User(username=username,email=email,password=password,is_admin=is_admin)
        user.save()
        if is_admin == False:
            return redirect('books')
        else:
            return redirect('adminpage')
    return render(request, 'library/signup.html')

def addbook(request):
    if request.method=='POST':
        name=request.POST.get('name')
        author=request.POST.get('author')
        description=request.POST.get('description')
        is_available=request.POST.get('is_available')
        is_borrowed=request.POST.get('is_borrowed')
        cover_page=request.POST.get('cover_page')
        categories=request.POST.get('categories')
    return render(request, 'library/adminpage.html')
