from django.shortcuts import render,redirect
from .forms import BrandCreateForm
from .models import Brands
from django.views.generic import TemplateView
# Create your views here.


# brand view
class BrandView(TemplateView):
    model=Brands
    form_class=BrandCreateForm
    template_name = "shop/brandcreate.html"
    context={}
    def get(self, request, *args, **kwargs):
        brands=self.model.objects.all()
        self.context["brands"]=brands
        self.context["form"]=self.form_class
        return render(request,self.template_name,self.context)

    def post(self, request, *args, **kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect("brandview")
        else:
            brands = self.model.objects.all()
            self.context["brands"] = brands
            self.context["form"] = self.form_class
            return render(request, self.template_name, self.context)


# brand edit
class BrandEdit(TemplateView):
    model=Brands
    form_class=BrandCreateForm
    template_name = "shop/brandcreate.html"
    context={}
    def get(self, request, *args, **kwargs):
        brand=self.model.objects.get(id=kwargs["id"])
        form=self.form_class(instance=brand)
        self.context["form"]=form
        return render(request,self.template_name,self.context)
    def post(self, request, *args, **kwargs):
        brand = self.model.objects.get(id=kwargs["id"])
        form = self.form_class(request.POST,instance=brand)
        if form.is_valid():
            form.save()
            return redirect("brandview")
        else:
            self.context["form"]=form
            return render(request, self.template_name, self.context)

# brand delete
class BrandDelete(TemplateView):
    model=Brands
    form_class=BrandCreateForm
    template_name = "shop/brandcreate.html"
    context = {}
    def get(self, request, *args, **kwargs):
        brand=self.model.objects.get(id=kwargs["id"])
        brand.delete()
        return redirect("brandview")