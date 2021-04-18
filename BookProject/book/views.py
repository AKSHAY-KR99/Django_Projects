from django.shortcuts import render,redirect
from .forms import BookCreateFrom,UserRegFrom,LoginForm
from .models import Book
from django.contrib.auth import authenticate,login

# Create your views here.
def book_create(request):
    form=BookCreateFrom()
    context={}
    context["form"]=form
    books=Book.objects.all()
    context["books"]=books
    if request.method=='POST':
        form=BookCreateFrom(request.POST)
        if form.is_valid():
            form.save()
            print("book object seved")
            return redirect("create")

        else:
            print("else")
            form=BookCreateFrom(request.POST)
            context["form"]=form
            return render(request,'book/bookcreate.html',context)


    return render(request,'book/bookcreate.html',context)


def book_delete(request,id):
    book=Book.objects.get(id=id)
    book.delete()
    return redirect("create")

def book_view(request,id):
    book=Book.objects.get(id=id)
    context={}
    context["book"]=book
    return render(request,"book/bookdetail.html",context)


def book_update(request,id):
    book=Book.objects.get(id=id)
    form=BookCreateFrom(instance=book)
    context={}
    context['form']=form
    if request.method=='POST':
        form=BookCreateFrom(request.POST,instance=book)
        if form.is_valid():
            form.save()
            return redirect("create")


    return render(request,"book/bookedit.html",context)


def registration(request):
    form=UserRegFrom
    context={}
    context["form"]=form
    if request.method=='POST':
        form=UserRegFrom(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'book/login.html',context)
        else:
            form=UserRegFrom(request.POST)
            context["form"]=form
            return render(request, 'book/registration.html', context)
    return render(request,'book/registration.html',context)

def login_view(request):
    form=LoginForm()
    context={}
    context["form"]=form

    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            user=authenticate(username=username,password=password)
            if user:
                print("login Successfull")
                login(request,user)
                return redirect("create")
            else:
                print("fails")
                return render(request, 'book/login.html', context)

    return render(request,'book/login.html',context)
