from django.shortcuts import render, redirect

from django.views.generic import TemplateView

from .models import EventCategory, Event, EventBook, Feedback
from .forms import EventCategoryForm, EventCreationFrom, UserRegistrationForm, EventBookingForm, Feedbackform

from django.contrib.auth import login, logout, authenticate


# Create your views here.

class EventCategoryView(TemplateView):
    model = EventCategory
    form_class = EventCategoryForm
    template_name = 'event/event_category.html'
    context = {}

    def get(self, request, *args, **kwargs):
        events = self.model.objects.all()
        self.context["events"] = events
        self.context["form"] = self.form_class
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect("category")
        else:
            events = self.model.objects.all()
            self.context["events"] = events
            self.context["form"] = self.form_class
            return render(request, self.template_name, self.context)


class EventCategoryEdit(TemplateView):
    model = EventCategory
    form_class = EventCategoryForm
    template_name = "event/event_category.html"
    context = {}

    def get(self, request, *args, **kwargs):
        event = self.model.objects.get(id=kwargs["id"])
        form = self.form_class(instance=event)
        self.context["form"] = form
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        event = self.model.objects.get(id=kwargs["id"])
        form = self.form_class(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect("category")
        else:
            self.context["form"] = form
            return render(request, self.template_name, self.context)


class EventCategoryDelete(TemplateView):
    model = EventCategory
    form_class = EventCategoryForm
    template_name = "event/event_category.html"
    context = {}

    def get(self, request, *args, **kwargs):
        event = self.model.objects.get(id=kwargs["id"])
        event.delete()
        return redirect("category")


class EventCreationView(TemplateView):
    model = Event
    form_class = EventCreationFrom
    template_name = 'event/eventcreation.html'
    context = {}

    def get(self, request, *args, **kwargs):
        form = self.form_class
        self.context["form"] = form
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        form = EventCreationFrom(request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect("eventcreation")
        else:
            self.context["form"] = form
            return render(request, self.template_name, self.context)


class ListEvents(TemplateView):
    model = Event
    template_name = "event/eventlist.html"
    context = {}

    def get(self, request, *args, **kwargs):
        events = self.model.objects.all()
        self.context["events"] = events
        return render(request, self.template_name, self.context)


class ViewEventDetails(TemplateView):
    model = Event
    template_name = 'event/view_details.html'
    context = {}

    def get(self, request, *args, **kwargs):
        event = self.model.objects.get(id=kwargs["id"])
        self.context['event'] = event
        return render(request, self.template_name, self.context)


class EventEditListAdmin(TemplateView):
    model = Event
    template_name = 'event/admin_only.html'
    context = {}

    def get(self, request, *args, **kwargs):
        event = self.model.objects.all()
        self.context['events'] = event
        return render(request, self.template_name, self.context)


class EditEventForm(TemplateView):
    model = Event
    form_class = EventCreationFrom
    template_name = 'event/eventcreation.html'
    context = {}

    def get(self, request, *args, **kwargs):
        event = self.model.objects.get(id=kwargs["id"])
        form = self.form_class(instance=event)
        self.context["form"] = form
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        event = self.model.objects.get(id=kwargs["id"])
        form = self.form_class(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('eventedit')
        else:
            self.context['form'] = form
            return render(request, self.template_name, self.context)


class DeleteEventForm(TemplateView):
    model = Event
    template_name = 'event/admin_only.html'

    def get(self, request, *args, **kwargs):
        event = self.model.objects.get(id=kwargs["id"])
        event.delete()
        return redirect('eventedit')


class UserRegistrationView(TemplateView):
    form_class = UserRegistrationForm
    template_name = "event/user_registration.html"
    context = {}

    def get(self, request, *args, **kwargs):
        form = self.form_class
        self.context["form"] = form
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
        else:
            self.context["form"] = form
            return render(request, self.template_name, self.context)


class LogIn(TemplateView):
    template_name = "event/login.html"

    def post(self, request, *args, **kwargs):
        username = request.POST.get("uname")
        password = request.POST.get("pwd")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("eventlist")
        else:
            return render(request, self.template_name)


def user_logout(request):
    logout(request)
    return redirect("login")


class EventBookingView(TemplateView):
    model = EventBook
    form_class = EventBookingForm
    template_name = 'event/event_booking.html'
    context = {}

    def get(self, request, *args, **kwargs):
        events = Event.objects.get(id=kwargs['id'])
        form = self.form_class(initial={'event': events, 'user': request.user})
        self.context['form'] = form
        self.context['event'] = events
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        id = kwargs.get('id')
        form = self.form_class(request.POST)
        if form.is_valid():
            event = form.cleaned_data.get("event")
            user = form.cleaned_data.get("user")
            no_of_tickets = form.cleaned_data.get("no_of_tickets")
            mobile_number = form.cleaned_data.get("mobile_number")

            current_event = Event.objects.get(event_name=event)
            available = current_event.avlbl_seats
            price = current_event.ticket_price

            if ((no_of_tickets <= available) & (available > 0)):
                amount = no_of_tickets * price
                available -= no_of_tickets
                current_event.avlbl_seats = available
                bookings = self.model(event=event, user=user, no_of_tickets=no_of_tickets, mobile_number=mobile_number,
                                      total=amount)
                bookings.save()
                print("sucessaayittund ttooooo")
                return redirect("success", id=id)
            else:
                return render(request, 'event/failed.html')


        else:
            print('nooooo')
            events = Event.objects.get(id=kwargs['id'])
            form = self.form_class(initial={'event': events, 'user': request.user})
            self.context['form'] = form
            self.context['event'] = events
            return render(request, self.template_name, self.context)


class SuccessPage(TemplateView):
    model = EventBook
    template_name = 'event/succesfullBooking.html'
    context = {}

    def get(self, request, *args, **kwargs):
        id = kwargs.get('id')
        event = self.model.objects.get(id=id)
        self.context['event'] = event
        return render(request, self.template_name, self.context)


class Orders(TemplateView):
    model = EventBook
    template_name = 'event/orders.html'
    context = {}

    def get(self, request, *args, **kwargs):
        uname = request.user
        events = self.model.objects.all().filter(user=uname)
        self.context['events'] = events
        return render(request, self.template_name, self.context)


class OrderDetails(TemplateView):
    model = EventBook
    template_name = 'event/orderdetails.html'
    context = {}

    def get(self, request, *args, **kwargs):
        event = self.model.objects.get(id=kwargs['id'])
        self.context['event'] = event
        return render(request, self.template_name, self.context)


class AddFeedback(TemplateView):
    model = Feedback
    form_class = Feedbackform
    template_name = 'event/feedback.html'
    context = {}

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial={'user': request.user})
        self.context['form'] = form
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect("eventlist")
        else:
            form = self.form_class(initial={'user': request.user})
            self.context['form'] = form
            return render(request, self.template_name, self.context)


class ViewFeedBackAdmin(TemplateView):
    model=Feedback
    template_name = 'event/feebbackview.html'
    context={}
    def get(self, request, *args, **kwargs):
        fbs=self.model.objects.all()
        self.context['fbs']=fbs
        return render(request,self.template_name,self.context)