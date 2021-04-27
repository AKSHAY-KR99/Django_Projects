from django.shortcuts import render
from Bill.forms import OrderCreationForm
from django.views.generic import TemplateView
from Bill.models import Order
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