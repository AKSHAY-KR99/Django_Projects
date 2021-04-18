"""MobileApplication URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from .views import *

urlpatterns = [
    path("",lambda request:render(request,"shop/index.html")),
    path("brands",brand_view,name="brandview"),
    path("mobiles",create_mobile,name="createmobile"),
    path("mobiles/list",list_mobiles,name="listmobiles"),
    path("brands/delete/<int:id>",delete_brand,name="delete"),
    path("brands/edit/<int:id>",edit_brand,name="edit"),
    path("mobiles/detail/<int:id>",mobile_detail,name="detail"),
    path("mobiles/userregistration",user_registration,name="registration"),
    path("mobiles/login",user_login,name="userlogin"),
    path("mobiles/logout",user_logout,name="userlogout"),
    path("mobiles/order/<int:id>",order_item,name="orders"),
    path("mobiles/cart",cart,name="cart"),
    path("mobiles/edit_list",edit_mobile,name="editlist"),
    path("mobiles/edit_mobiledetails/<int:id>",edit_mobiledetails,name="editmobiledetails"),
    path("mobiles/delete_mobile/<int:id>",delete_mobile,name="delete_mobile"),
    path("error",error_page,name="error"),
    path("mobiles/products",product_list,name="product")
]
