from django.shortcuts import render,redirect
from .forms import BrandCreateForm,MobileCreateForm,UserRegFrom
from .models import Brands,Mobile
from django.views.generic import TemplateView
from django.contrib.auth import authenticate,login,logout
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


# MobileCreations
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
class ListEditMobile(TemplateView):
    model = Mobile
    template_name = "shop/edit_list.html"
    context = {}
    def get(self, request, *args, **kwargs):
        mobiles=self.model.objects.all()
        self.context["mobiles"]=mobiles
        return render(request,self.template_name,self.context)


# deletemobile
class DeleteMobile(TemplateView):
    model = Mobile
    template_name = "shop/edit_list.html"
    context = {}
    def get(self, request, *args, **kwargs):
        mobile=self.model.objects.get(id=kwargs["id"])
        mobile.delete()
        return redirect("editlist")


# edit Mobiles
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
class ListMobile(TemplateView):
    model = Mobile
    template_name = "shop/listmobiles.html"
    context = {}
    def get(self, request, *args, **kwargs):
        mobiles=self.model.objects.all()
        self.context["mobiles"]=mobiles
        return render(request,self.template_name,self.context)


# view the mobiles
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

