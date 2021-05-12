"""Product_Project URL Configuration

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

from django.urls import path
from .views import ProductViews, CartProductDetails, CartCancel, CartView, OrderItem, user_logout, LogIn, \
    UserRegistration, EditMobiles, BrandView, BrandEdit, BrandDelete, CreateMobile, ListMobile, ViewMobile, \
    ListEditMobile, DeleteMobile, error_page

urlpatterns = [
    path("error",error_page,name="error"),
    path("brands",BrandView.as_view(),name="brandview"),
    path("brands/edit/<int:id>",BrandEdit.as_view(),name="brandedit"),
    path("brands/delete/<int:id>",BrandDelete.as_view(),name="branddelete"),
    path("mobiles",CreateMobile.as_view(),name="createmobile"),
    path("mobiles/list",ListMobile.as_view(),name="listmobiles"),
    path("mobiles/view/<int:id>",ViewMobile.as_view(),name="viewmobile"),
    path("mobiles/editlist",ListEditMobile.as_view(),name="editlist"),
    path("mobiles/del-mobile/<int:id>",DeleteMobile.as_view(),name="deletemobile"),
    path("mobiles/edit-mobile/<int:id>",EditMobiles.as_view(),name="editmobile"),
    path("mobiles/user-reg",UserRegistration.as_view(),name="userregistration"),
    path("mobiles/login",LogIn.as_view(),name="userlogin"),
    path("mobiles/logout",user_logout,name="userlogout"),
    path("mobiles/order-item/<int:id>",OrderItem.as_view(),name="orderitem"),
    path("mobiles/cart",CartView.as_view(),name="cartview"),
    path("mobiles/cart/cancel/<int:id>",CartCancel.as_view(),name="cartcancel"),
    path("mobiles/cart/view/<int:id>",CartProductDetails.as_view(),name="cartitemview"),
    path("mobiles/products",ProductViews.as_view(),name="products")

]
