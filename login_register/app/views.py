from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Book, Author
from .book_serializer import Book_Serializer
from .forms import BookForm, AuthorForm
from django.http import HttpResponseRedirect, HttpResponse


# Create your views here.

def indexView(request):
    return render(request, 'index.html')


@login_required
def dashboardView(request):
    books = Book.objects.all()
    serializer = Book_Serializer(books, many=True)
    context = {'books': books}
    return render(request, 'dashboard.html', context)


def registerView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registration/login.html')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


def books(request):
    if request.method == "GET":
        data = Book.objects.all()
        #return HttpResponse(data)
        return render(request, 'books.html', {'data': data})
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid:
            form.save()
            return HttpResponse('new book has been created successfully')
        return HttpResponse("please fill the details properly")

def authors(request):
    data = Author.objects.all()
    # return HttpResponse(data)
    return render(request, 'books.html', {'data': data})


# def bookView(request):
#     form = BookForm(request)
#     if request.method == "POST":
#         form = BookForm(request.POST)
#         if form.is_valid:
#             form.save()
#             return HttpResponse('new book has been created successfully')
#     return render(request, 'book.html', {'form': form})

    # if request.method == "GET":
    #     # data = serializersBook_Serializer.objects.all()
    #     return HttpResponse('data')
