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

from Bill.views import OrderCreateView,SearchByName,OrderLineView,SelectSearch,SearchByBill,SearchByDate

urlpatterns = [
    path("create-order",OrderCreateView.as_view(),name="create-order"),
    path("orderline/<str:bill_num>",OrderLineView.as_view(),name="orderline"),
    path("searchby",SelectSearch.as_view(),name="searchby"),
    path("searchbybill",SearchByBill.as_view(),name="searchbybill"),
    path("searchbydate",SearchByDate.as_view(),name="searchbydate"),
    path("searchbyname",SearchByName.as_view(),name="searchbyname")
]
