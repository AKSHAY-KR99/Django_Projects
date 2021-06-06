"""event_ticket_booking_system URL Configuration

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
from .views import EventCategoryView, EventCategoryEdit, EventCategoryDelete, EventCreationView, ListEvents, \
    ViewEventDetails, DeleteEventForm, EditEventForm, EventEditListAdmin, \
    UserRegistrationView, LogIn, user_logout, EventBookingView, SuccessPage,Orders,OrderDetails,\
    AddFeedback,ViewFeedBackAdmin

urlpatterns = [
    path('category', EventCategoryView.as_view(), name='category'),
    path('category/edit/<int:id>', EventCategoryEdit.as_view(), name='eventcategoryedit'),
    path('category/delete/<int:id>', EventCategoryDelete.as_view(), name='eventcategorydelete'),
    path('eventcreation', EventCreationView.as_view(), name='eventcreation'),
    path('eventlist', ListEvents.as_view(), name='eventlist'),
    path('eventlist/viewevent/<int:id>', ViewEventDetails.as_view(), name='viewevent'),
    path('eventedit', EventEditListAdmin.as_view(), name='eventedit'),
    path('eventedit/edit/<int:id>', EditEventForm.as_view(), name='editeventform'),
    path('eventedit/delete/<int:id>', DeleteEventForm.as_view(), name='deleteeventform'),
    path('user-reg', UserRegistrationView.as_view(), name='user-reg'),
    path('login', LogIn.as_view(), name='login'),
    path('logout', user_logout, name='logout'),
    path('eventlist/viewevent/bookevent/<int:id>', EventBookingView.as_view(), name='bookevent'),
    path('eventlist/success/<int:id>', SuccessPage.as_view(), name="success"),
    path('orders', Orders.as_view(), name='orders'),
    path('orderdetails/<int:id>',OrderDetails.as_view(),name='orderdetails'),
    path('feedback',AddFeedback.as_view(),name='feedback'),
    path('feedbackview',ViewFeedBackAdmin.as_view(),name='viewfeedback')
]
