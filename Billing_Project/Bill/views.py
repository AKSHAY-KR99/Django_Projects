from django.contrib.auth import login
from django.shortcuts import render,redirect
from Bill.forms import OrderCreationForm, OrderLineForm, UserRegForm, LoginForm
from django.views.generic import TemplateView
from Bill.models import Order,OrderLines,Purchase,Product
from django.contrib.auth.models import User
from .filters import OrderFilter
from .decorators import amdin_only
from django.db.models import Sum
from django.utils.decorators import method_decorator
from Bill.authentication import EmailAuthBackend
# Create your views here.



@method_decorator(amdin_only,name='dispatch')
class OrderCreateView(TemplateView):
    model=Order
    form_class=OrderCreationForm
    template_name = "bill/ordercreate.html"
    context={}
    def get(self, request, *args, **kwargs):
        form=self.form_class
        self.context["form"]=form
        order=self.model.objects.last()
        if order:
            last_billnum=order.bill_number
            last=int(last_billnum.split("-")[1])+1
            bill_number="LULU-"+str(last)

        else:
            bill_number="LULU-1000"
        form = self.form_class(initial={"bill_number":bill_number})
        self.context["form"] = form
        return render(request,self.template_name,self.context)

    def post(self, request, *args, **kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            bill_number=form.cleaned_data.get("bill_number")
            form.save()
            return redirect("orderline",bill_num=bill_number)



@method_decorator(amdin_only,name='dispatch')
class OrderLineView(TemplateView):
    model = OrderLines
    form_class = OrderLineForm
    template_name = "bill/orderline.html"
    context={}

    def get(self, request, *args, **kwargs):
        bill_number=kwargs.get("bill_num")

        form=self.form_class(initial={"bill_number":bill_number})
        self.context["form"]=form
        querySet = self.model.objects.filter(bill_number__bill_number=bill_number)
        total = OrderLines.objects.filter(bill_number__bill_number=bill_number).aggregate(Sum('amount'))
        ctotal=total["amount__sum"]
        self.context["total"]=ctotal
        self.context["items"]=querySet
        self.context["bill_number"]=bill_number
        return render(request,self.template_name,self.context)

    def post(self, request, *args, **kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():

            bill_number=form.cleaned_data.get("bill_number")
            bill = Order.objects.get(bill_number=bill_number)

            product_name=form.cleaned_data.get("product_name")
            prdt = Product.objects.get(product_name=product_name)

            qty=form.cleaned_data.get("product_qty")

            product=Purchase.objects.get(product__product_name=product_name) #to get selling price
            amount=product.selling_price*qty

            orderline=self.model(bill_number=bill,product=prdt,product_qty=qty,amount=amount)
            orderline.save()
            print("Saved...!")
            return redirect("orderline", bill_num=bill_number)



@method_decorator(amdin_only,name='dispatch')
class BillGenerate(TemplateView):
    def get(self, request, *args, **kwargs):
        bill_number=kwargs.get("billnum")
        total = OrderLines.objects.filter(bill_number__bill_number=bill_number).aggregate(Sum('amount'))
        grandtotal = total["amount__sum"]
        order=Order.objects.get(bill_number=bill_number)
        order.bill_total=grandtotal
        order.save()
        querySet = OrderLines.objects.filter(bill_number__bill_number=bill_number)
        context={}
        context["items"]=querySet
        context["total"]=grandtotal
        return render(request,"bill/customer_bill.html",context)


# @method_decorator(amdin_only,name='dispatch')
class SearchView(TemplateView):
    model=Order
    template_name = "bill/search.html"
    context={}
    def get(self, request, *args, **kwargs):
        orders=self.model.objects.all()
        orderfilter=OrderFilter(request.GET,queryset=orders)
        self.context['filter']=orderfilter
        return render(request,self.template_name,self.context)



class UserRegView(TemplateView):
    model=User
    form_class=UserRegForm
    template_name = "bill/userreg.html"
    context={}
    def get(self, request, *args, **kwargs):
        form=self.form_class()
        self.context["form"]=form
        return render(request,self.template_name,self.context)

    def post(self, request, *args, **kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect("userlogin")
        else:
            print("noooo")


class UserLogin(TemplateView):
    form_class=LoginForm
    template_name = "bill/login.html"
    context={}
    def get(self, request, *args, **kwargs):
        form=self.form_class()
        self.context["form"]=form
        return render(request,self.template_name,self.context)

    def post(self, request, *args, **kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            email=form.cleaned_data.get("email")
            password=form.cleaned_data.get("password")
            obj=EmailAuthBackend()
            user=obj.authenticate(request,username=email,password=password)
            if user:
                login(request,user)

            return redirect("home")



class HomePageView(TemplateView):
    template_name = "bill/home.html"
    def get(self, request, *args, **kwargs):
        return render(request,self.template_name)








