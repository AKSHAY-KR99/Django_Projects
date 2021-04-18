from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render,redirect

from student.forms import studentRegistrationForm,studentLogin
from .models import Student
# templates

# def prime(request):
#     return render(request,"math/prime.html")
#
# def check(request):
#     num=int(request.POST.get("input"))
#     c = 0
#     for i in range(2, num):
#         if (num % i == 0):
#             c = c + 1
#         else:
#             pass
#     if(c==0):
#         print("give number is prime")
#     else:
#         print("given number is not prime")
#     return render(request,"math/prime.html")
#
 # def stud_register(request):
 #    return render(request,"student/studlogin.html")
#
# def registration(request):
#     name=request.POST.get("name")
#     email=request.POST.get("email")
#     course=request.POST.get("crse")
#     print(name,course,email)
#     # dictionary comon name:context
#     return render(request, "student/studlogin.html")
#
# def stud_login(request):
#     return HttpResponse("<h1>welcome to student login</h1>")
#
# def stud_timetable(request):
#     return HttpResponse("<h1>welcome to student timetable</h1>")
#
# def post_feedback(request):
#     return HttpResponse("<h1>welcome to student feedback</h1>")



# registration http methode :::: get=>load html page ::::: post=>store the data


def registration(request):
    form=studentRegistrationForm()  # created a object of student register
    context={}
    context["form"]=form
    student=Student.objects.all()
    context["student"]=student
    if request.method=='POST':
        form=studentRegistrationForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data.get("name")
            email=form.cleaned_data.get("email")
            phone= form.cleaned_data.get("phone")
            username =form.cleaned_data.get("username")
            password =form.cleaned_data.get("password")
            student=Student(name=name,email=email,phone=phone,username=username,password=password)
            student.save()
            print("Data Registered")
            return redirect("register")
        else:
            form=studentRegistrationForm(request.POST)
            context["form"]=form
            return render(request, "student/registerstudent.html", context)



    return render(request,"student/registerstudent.html",context)


def login_view(request):
    form=studentLogin()
    context={}
    context["form"]=form
    if request.method=='POST':
        form=studentLogin(request.POST)
        if(form.is_valid()):
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            print(username,"<=>",password)
            return render(request, "student/studlogin.html", context)

    return render(request,"student/studlogin.html",context)


def stud_delete(request,id):
    stud=Student.objects.get(id=id)
    stud.delete()
    return redirect("register")