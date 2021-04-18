from django.shortcuts import render

# Create your views here.

def listprime(request):
    return render(request,"listprime.html")

def list(request):
    num1=int(request.POST.get("num1"))
    num2=int(request.POST.get("num2"))
    context={}
    for num in range(num1,num2):
        for i in range(2,num):
            if(num%i==0):
                break
            else:
                print(num)
                context["res"]=num
    return render(request,"listprime.html",context)