from django.shortcuts import render,redirect
from .forms import BookCreateFrom,UserRegFrom,LoginForm
from .models import Book
from django.contrib.auth import authenticate,login

from django.views.generic import TemplateView,ListView,CreateView,UpdateView,DetailView,DeleteView
from django.urls import reverse_lazy



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



# list_view

# create_view

# detial_view

# update_view

# delete_view

# listing of all books
class Books(TemplateView):
    model = Book
    template_name = "book/bookcreate.html"
    context={}
    def get(self, request, *args, **kwargs):
        books=self.model.objects.all()
        self.context["books"]=books
        return render(request,self.template_name,self.context)

# create view
class BookCreate(TemplateView):
    model = Book
    form_class = BookCreateFrom
    template_name = "book/bookcreate.html"
    context={}
    def get(self, request, *args, **kwargs):
        self.context["form"]=self.form_class
        return render(request,self.template_name,self.context)
    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect("clslist")
        else:
            self.context["form"]=form
            return render(request, self.template_name, self.context)

# updation of books
class BookUpdateView(TemplateView):
    model = Book
    form_class = BookCreateFrom
    template_name = "book/bookedit.html"
    context={}
    def get_object(self,id):
        return self.model.objects.get(id=id)

    def get(self, request, *args, **kwargs):
        book=self.get_object(kwargs["pk"])
        form=self.form_class(instance=book)
        self.context["form"]=form
        return render(request,self.template_name,self.context)
    def post(self, request, *args, **kwargs):
        book=self.get_object(kwargs["pk"])
        form=self.form_class(request.POST,instance=book)
        if form.is_valid():
            form.save()
            return redirect("clslist")
        else:
            self.context["form"]=form
            return render(request, self.template_name, self.context)


# book detail
class BookDetail(TemplateView):
    model = Book
    template_name = "book/bookdetail.html"
    context={}
    def get(self, request, *args, **kwargs):
        book=self.model.objects.get(id=kwargs["pk"])
        self.context["book"]=book
        return render(request,self.template_name,self.context)



# delete
class BookDelete(TemplateView):
    model = Book
    template_name = "book/bookdelete.html"
    context={}
    def get(self, request, *args, **kwargs):
        book = self.model.objects.get(id=kwargs["pk"])
        book.delete()
        return redirect("clslist")


