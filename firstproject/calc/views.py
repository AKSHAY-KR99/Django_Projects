from django.shortcuts import render

# Create your views here.
def getCalc(request):
    return render(request,"calculation.html")

def solve(request):
    num1=int(request.POST.get("num1"))
    num2=int(request.POST.get("num2"))
    add=num1+num2
    print(add)
    context={}
    context["res"]=add
    return render(request, "calculation.html",context)

def substract(request):
    return render(request,"substarct.html")

def sub(request):
    num1=int(request.POST.get("num1"))
    num2=int(request.POST.get("num2"))
    sub=num1-num2
    context={}
    context["res"]=sub
    return render(request,"substarct.html",context)