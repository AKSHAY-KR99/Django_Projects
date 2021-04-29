from django.shortcuts import render,redirect
from Bill.forms import OrderCreationForm,OrderLineForm,SearchByBillNumber,SearchByDateForm,SearchByNameForm
from django.views.generic import TemplateView
from Bill.models import Order,OrderLines,Purchase,Product

from django.db.models import Sum
# Create your views here.

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




class SelectSearch(TemplateView):
    template_name = "bill/selectsearchtype.html"
    def get(self, request, *args, **kwargs):
        return render(request,self.template_name)



class SearchByBill(TemplateView):
    model=OrderLines
    form_class=SearchByBillNumber
    template_name = "bill/searchbybill.html"
    context={}
    def get(self, request, *args, **kwargs):
        form=self.form_class
        self.context["form"]=form
        return render(request,self.template_name,self.context)
    def post(self, request, *args, **kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            bill_num=form.cleaned_data.get("bill_number")
        orders=self.model.objects.filter(bill_number__bill_number=bill_num)
        self.context['orders']=orders
        return redirect("searchbybill")


class SearchByDate(TemplateView):
    model=OrderLines
    form_class=SearchByDateForm
    template_name = "bill/searchbydate.html"
    context={}
    def get(self, request, *args, **kwargs):
        form=self.form_class
        self.context["form"]=form
        return render(request,self.template_name,self.context)

    def post(self, request, *args, **kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            date=form.cleaned_data.get("date")
        orders=self.model.objects.filter(bill_number__bill_date=date)
        self.context["orders"]=orders
        return redirect("searchbydate")




class SearchByName(TemplateView):
    model=OrderLines
    form_class=SearchByNameForm
    template_name = "bill/searchbyname.html"
    context={}
    def get(self, request, *args, **kwargs):
        form=self.form_class
        self.context["form"]=form
        return render(request,self.template_name,self.context)
    def post(self, request, *args, **kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            name=form.cleaned_data.get("customer_name")
        orders=self.model.objects.filter(bill_number__customer_name=name)
        self.context["orders"]=orders
        return redirect("searchbyname")