"""Event_App URL Configuration

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

from event.views import show_hipe,EventCategoryView,EventEdit,EventDelete,EventCreationView,ListEvents,\
        EventEditListAdmin,EditEventForm,DeleteEventForm,ViewEventDetails

urlpatterns = [
        path("",show_hipe),
        path('category',EventCategoryView.as_view(),name='category'),
        path('category/edit/<int:id>',EventEdit.as_view(),name='eventedit'),
        path('category/delete/<int:id>',EventDelete.as_view(),name='eventdelete'),
        path('eventcreation',EventCreationView.as_view(),name='eventcreation'),
        path('eventlist',ListEvents.as_view(),name='eventlist'),
        path('eventedit',EventEditListAdmin.as_view(),name='eventedit'),
        path('eventedit/edit/<int:id>',EditEventForm.as_view(),name='editeventform'),
        path('eventedit/delete/<int:id>',DeleteEventForm.as_view(),name='deleteeventform'),
        path('eventlist/viewevent/<int:id>',ViewEventDetails.as_view(),name='viewevent')



]
