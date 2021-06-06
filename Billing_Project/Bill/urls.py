"""Billing_Project URL Configuration

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
from Bill.views import SearchView, OrderCreateView, OrderLineView, BillGenerate, UserRegView, UserLogin, HomePageView

urlpatterns = [
    path("create-order",OrderCreateView.as_view(),name="create-order"),
    path("orderline/<str:bill_num>",OrderLineView.as_view(),name="orderline"),
    path("genertebill/<str:billnum>" ,BillGenerate.as_view(),name="completeorder"),
    path("search",SearchView.as_view(),name="search"),
    path("error",lambda request:render(request,"bill/error.html"),name="error"),
    path("user-reg",UserRegView.as_view(),name="user-reg"),
    path("login",UserLogin.as_view(),name="userlogin"),
    path("home",HomePageView.as_view(),name="home")
]
