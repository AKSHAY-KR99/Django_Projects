"""restbook URL Configuration

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
from .views import book_list, book_details,BookList,BookDetails,BookListMixin,BookDetailMixin

urlpatterns = [
        path("fbooks/",book_list),
        path("fbooks/<int:id>",book_details),
        path("books/",BookList.as_view()),
        path("books/<int:id>",BookDetails.as_view()),
        path("mixinbook/",BookListMixin.as_view()),
        path("mixinbook/<int:pk>",BookDetailMixin.as_view())

]
