from django.shortcuts import render,redirect

# Create your views here.

# Brands management



from shop.forms import BrandCreateForm,MobileCreateForm,UserRegForm,OrderForm
from .models import Brands,Mobile,Order
from django.contrib.auth import authenticate,login,logout
from .decorators import admin_permission_not_required_id,admin_permission_required,admin_permission_required_id,login_authentication_id,login_authentication

@admin_permission_required
def brand_view(request):
    brands=Brands.objects.all()
    form=BrandCreateForm()
    context={}
    context["brands"]=brands
    context["form"]=form
    if request.method=='POST':
        form=BrandCreateForm(request.POST)
        if form.is_valid():
            form.save()
            print("saved")
            return redirect("brandview")
    return render(request,"shop/brandcreate.html",context)

@admin_permission_required
def create_mobile(request):

    form=MobileCreateForm()
    context={}
    context["form"]=form
    if request.method=='POST':
        form=MobileCreateForm(request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            print("saved")
            return redirect("createmobile")
    return render(request,"shop/mobilecreate.html",context)


@login_authentication
def list_mobiles(request):
    mobiles=Mobile.objects.all()
    context={}
    context["mobiles"]=mobiles
    return render(request,"shop/listmobiles.html",context)

@admin_permission_required_id
def delete_brand(request,id):
    if request.user.is_superuser:
        brand=Brands.objects.get(id=id)
        brand.delete()
        return redirect("brandview")
    else:
        return redirect("error")

@admin_permission_required_id
def edit_brand(request,id):
    if request.user.is_superuser:
        brand=Brands.objects.get(id=id)
        form=BrandCreateForm(instance=brand)
        context={}
        context["form"]=form
        if request.method=='POST':
            form=BrandCreateForm(request.POST,instance=brand)
            if form.is_valid():
                form.save()
                return redirect("brandview")
        return render(request,"shop/brandcreate.html",context)
    else:
        return redirect("error")

@login_authentication_id
def mobile_detail(request,id):
    mobile=Mobile.objects.get(id=id)
    context={}
    context["mobile"]=mobile
    return render(request,"shop/mobiledetail.html",context)


def user_registration(request):
    form=UserRegForm()
    context={}
    context["form"]=form
    if request.method=="POST":
        form=UserRegForm(request.POST)
        if form.is_valid():
            form.save()
            print("saved")
            return redirect("userlogin")
        else:
            form=UserRegForm(request.POST)
            context["form"]=form
            print("error")
            return render(request,"shop/userreg.html",context)


    return render(request,"shop/userreg.html",context)


def user_login(request):
    if request.method=="POST":
        username=request.POST.get("uname")
        password=request.POST.get("pwd")
        user=authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            return redirect("listmobiles")
        else:
            return render(request,"shop/login.html")

    return render(request,"shop/login.html")


def user_logout(request):
    logout(request)
    return redirect("userlogin")

@login_authentication_id
def order_item(request,id):
    product=Mobile.objects.get(id=id)
    form = OrderForm(initial={"product": product,"user": request.user})
    context={}
    context["form"]=form
    context["product"]=product
    if request.method=='POST':
        form=OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("cart")
        else:
            form=OrderForm(request.POST)
            context["form"]=form
            context["product"]=product
            return render(request, "shop/order.html", context)
    return render(request, "shop/order.html", context)


@login_authentication
def cart(request):
    username=request.user
    orders=Order.objects.all().filter(user=username)
    for order in orders:
        print(order.product,order.user,order.status)
    context={}
    context["orders"]=orders
    return render(request,"shop/cart.html",context)


@admin_permission_required
def edit_mobile(request):
    mobiles=Mobile.objects.all()
    context={}
    context["mobiles"]=mobiles
    return render(request,"shop/edit_list.html",context)

@admin_permission_required_id
def edit_mobiledetails(request,id):
    if request.user.is_superuser:
        mobile=Mobile.objects.get(id=id)
        form=MobileCreateForm(instance=mobile)
        context={}
        context["form"]=form
        if request.method=='POST':
            form=MobileCreateForm(request.POST,instance=mobile)
            if form.is_valid():
                form.save()
                return redirect("createmobile")
        return render(request,"shop/mobilecreate.html",context)
    else:
        return redirect("error")


@admin_permission_required_id
def delete_mobile(request,id):
    if request.user.is_superuser:
        mobile=Mobile.objects.get(id=id)
        mobile.delete()
        return redirect("createmobile")
    else:
        return redirect("error")

def error_page(request):
    return render(request,"shop/errorpage.html")

@login_authentication
def product_list(request):
    products=Mobile.objects.all()
    context={}
    context["products"]=products
    return render(request,"shop/product_list.html",context)


@login_authentication_id
@admin_permission_not_required_id
def order_cancel(request,id):
    mobile=Order.objects.get(id=id)
    form=OrderForm(instance=mobile)
    context={}
    context["form"]=form
    if request.method=='POST':
        form=OrderForm(request.POST,instance=mobile)
        if form.is_valid():
            form.save()
            return redirect("cart")
        else:
            form=OrderForm(request.POST)
            context["form"]=form
            return render(request, "shop/order.html", context)
    return render(request,"shop/order_cancel.html",context)

@login_authentication_id
def view_order_item(request,id):
    order=Order.objects.get(id=id)
    context={}
    context["order"]=order
    return render(request,"shop/view_order_item.html",context)