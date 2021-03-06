from django.shortcuts import render,redirect
from .forms import BrandCreateForm,MobileCreateForm,UserRegFrom,OrderForm
from .models import Brands,Mobile,Order
from django.views.generic import TemplateView
from django.contrib.auth import authenticate,login,logout
from .decorators import amdin_only,user_authenticated,no_admin
from django.utils.decorators import method_decorator
# Create your views here.


# brand view
@method_decorator(user_authenticated,name='dispatch')
@method_decorator(amdin_only,name='dispatch')
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
@method_decorator(user_authenticated,name='dispatch')
@method_decorator(amdin_only,name='dispatch')
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
@method_decorator(user_authenticated,name='dispatch')
@method_decorator(amdin_only,name='dispatch')
class BrandDelete(TemplateView):
    model=Brands
    form_class=BrandCreateForm
    template_name = "shop/brandcreate.html"
    context = {}
    def get(self, request, *args, **kwargs):
        brand=self.model.objects.get(id=kwargs["id"])
        brand.delete()
        return redirect("brandview")


# MobileCreations
@method_decorator(user_authenticated,name='dispatch')
@method_decorator(amdin_only,name='dispatch')
class CreateMobile(TemplateView):
    model=Mobile
    form_class=MobileCreateForm
    template_name = "shop/mobilecreate.html"
    context={}
    def get(self, request, *args, **kwargs):
        form=self.form_class
        self.context["form"]=form
        return render(request,self.template_name,self.context)
    def post(self, request, *args, **kwargs):
        form=MobileCreateForm(request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect("createmobile")
        else:
            self.context["form"]=form
            return render(request, self.template_name, self.context)


# editMobilesSpec
@method_decorator(user_authenticated,name='dispatch')
@method_decorator(amdin_only,name='dispatch')
class ListEditMobile(TemplateView):
    model = Mobile
    template_name = "shop/edit_list.html"
    context = {}
    def get(self, request, *args, **kwargs):
        mobiles=self.model.objects.all()
        self.context["mobiles"]=mobiles
        return render(request,self.template_name,self.context)


# deletemobile
@method_decorator(user_authenticated,name='dispatch')
@method_decorator(amdin_only,name='dispatch')
class DeleteMobile(TemplateView):
    model = Mobile
    template_name = "shop/edit_list.html"
    context = {}
    def get(self, request, *args, **kwargs):
        mobile=self.model.objects.get(id=kwargs["id"])
        mobile.delete()
        return redirect("editlist")


# edit Mobiles
@method_decorator(user_authenticated,name='dispatch')
@method_decorator(amdin_only,name='dispatch')
class EditMobiles(TemplateView):
    model = Mobile
    form_class=MobileCreateForm
    template_name = "shop/mobilecreate.html"
    context = {}
    def get(self, request, *args, **kwargs):
        mobile=self.model.objects.get(id=kwargs["id"])
        form=self.form_class(instance=mobile)
        self.context["form"]=form
        return render(request,self.template_name,self.context)

    def post(self, request, *args, **kwargs):
        mobile = self.model.objects.get(id=kwargs["id"])
        form=self.form_class(request.POST,instance=mobile)
        if form.is_valid():
            form.save()
            return redirect("createmobile")
        else:
            self.context["form"]=form
            return render(request, self.template_name, self.context)


# mobilelist
@method_decorator(user_authenticated,name='dispatch')
class ListMobile(TemplateView):
    model = Mobile
    template_name = "shop/listmobiles.html"
    context = {}
    def get(self, request, *args, **kwargs):
        mobiles=self.model.objects.all()
        self.context["mobiles"]=mobiles
        return render(request,self.template_name,self.context)


# view the mobiles
@method_decorator(user_authenticated,name='dispatch')
class ViewMobile(TemplateView):
    model = Mobile
    template_name = "shop/mobiledetail.html"
    context = {}
    def get(self, request, *args, **kwargs):
        mobile=self.model.objects.get(id=kwargs["id"])
        self.context["mobile"]=mobile
        return render(request,self.template_name,self.context)


# userRegistration
class UserRegistration(TemplateView):
    form_class=UserRegFrom
    template_name = "shop/userreg.html"
    context={}
    def get(self, request, *args, **kwargs):
        form = self.form_class
        self.context["form"]=form
        return render(request,self.template_name,self.context)
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect("userlogin")
        else:
            self.context["form"]=form
            return render(request, self.template_name, self.context)



class LogIn(TemplateView):
    template_name = "shop/login.html"
    def post(self, request, *args, **kwargs):
        username = request.POST.get("uname")
        password = request.POST.get("pwd")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request,user)
            return redirect("listmobiles")
        else:
            return render(request,self.template_name)


def user_logout(request):
    logout(request)
    return redirect("userlogin")

@method_decorator(no_admin,name='dispatch')
@method_decorator(user_authenticated,name='dispatch')
class OrderItem(TemplateView):
    model=Mobile
    form_class=OrderForm
    template_name = "shop/order.html"
    context={}
    def get(self, request, *args, **kwargs):
        product=self.model.objects.get(id=kwargs["id"])
        self.context["product"]=product
        form=self.form_class(initial={"product": product,"user": request.user})
        self.context["form"]=form
        return render(request,self.template_name,self.context)
    def post(self, request, *args, **kwargs):
        form=OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("cartview")
        else:
            product = self.model.objects.get(id=kwargs["id"])
            self.context["product"] = product
            form = self.form_class(initial={"product": product, "user": request.user})
            self.context["form"] = form
            return render(request, self.template_name, self.context)


@method_decorator(user_authenticated,name='dispatch')
class CartView(TemplateView):
    model=Order
    template_name = "shop/cart.html"
    context={}
    def get(self, request, *args, **kwargs):
        username=request.user
        orders=self.model.objects.all().filter(user=username)
        self.context["orders"]=orders
        return render(request,self.template_name,self.context)

@method_decorator(no_admin,name='dispatch')
@method_decorator(user_authenticated,name='dispatch')
class CartCancel(TemplateView):
    model=Order
    form_class=OrderForm
    template_name = "shop/order_cancel.html"
    context={}
    def get(self, request, *args, **kwargs):
        mobile=self.model.objects.get(id=kwargs["id"])
        form=self.form_class(instance=mobile)
        self.context["form"]=form
        return render(request,self.template_name,self.context)
    def post(self, request, *args, **kwargs):
        mobile = self.model.objects.get(id=kwargs["id"])
        form=self.form_class(request.POST,instance=mobile)
        if form.is_valid():
            form.save()
            return redirect("cartview")
        else:
            form=OrderForm(request.POST)
            self.context["form"]=form
            return render(request, self.template_name, self.context)


@method_decorator(user_authenticated,name='dispatch')
class CartProductDetails(TemplateView):
    model=Order
    template_name = "shop/view_order_item.html"
    context={}
    def get(self, request, *args, **kwargs):
        order=self.model.objects.get(id=kwargs["id"])
        self.context["order"]=order
        return render(request,self.template_name,self.context)



@method_decorator(user_authenticated,name='dispatch')
class ProductViews(TemplateView):
    model=Mobile
    template_name = "shop/product_list.html"
    context={}
    def get(self, request, *args, **kwargs):
        products=self.model.objects.all()
        self.context["products"]=products
        return render(request,self.template_name,self.context)


def error_page(request):
    return render(request,"shop/errorpage.html")




