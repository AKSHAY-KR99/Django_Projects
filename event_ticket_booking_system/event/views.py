from django.utils.dateparse import parse_date
from django.db.models import Sum
from django.shortcuts import render, redirect

from django.views.generic import TemplateView

from .models import EventCategory, Event, EventBook, Feedback
from .forms import EventCategoryForm, EventCreationFrom, UserRegistrationForm, EventBookingForm, \
    Feedbackform, DailyCollectionBydate
from .filters import EventFilter

from django.contrib.auth import login, logout, authenticate

from .decorators import amdin_only, user_authenticated, no_amdin
from django.utils.decorators import method_decorator


# Create your views here.
@method_decorator(user_authenticated, name='dispatch')
@method_decorator(amdin_only, name='dispatch')
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


@method_decorator(user_authenticated, name='dispatch')
@method_decorator(amdin_only, name='dispatch')
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


@method_decorator(user_authenticated, name='dispatch')
@method_decorator(amdin_only, name='dispatch')
class EventCategoryDelete(TemplateView):
    model = EventCategory
    form_class = EventCategoryForm
    template_name = "event/event_category.html"
    context = {}

    def get(self, request, *args, **kwargs):
        event = self.model.objects.get(id=kwargs["id"])
        event.delete()
        return redirect("category")


@method_decorator(user_authenticated, name='dispatch')
@method_decorator(amdin_only, name='dispatch')
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


@method_decorator(user_authenticated, name='dispatch')
class ListEvents(TemplateView):
    model = Event
    template_name = "event/eventlist.html"
    context = {}

    def get(self, request, *args, **kwargs):
        events = self.model.objects.all()
        self.context["events"] = events
        return render(request, self.template_name, self.context)


@method_decorator(user_authenticated, name='dispatch')
class ViewEventDetails(TemplateView):
    model = Event
    template_name = 'event/view_details.html'
    context = {}

    def get(self, request, *args, **kwargs):
        event = self.model.objects.get(id=kwargs["id"])
        self.context['event'] = event
        return render(request, self.template_name, self.context)


@method_decorator(user_authenticated, name='dispatch')
@method_decorator(amdin_only, name='dispatch')
class EventEditListAdmin(TemplateView):
    model = Event
    template_name = 'event/admin_only.html'
    context = {}

    def get(self, request, *args, **kwargs):
        event = self.model.objects.all()
        self.context['events'] = event
        return render(request, self.template_name, self.context)


@method_decorator(user_authenticated, name='dispatch')
@method_decorator(amdin_only, name='dispatch')
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


@method_decorator(user_authenticated, name='dispatch')
@method_decorator(amdin_only, name='dispatch')
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


@method_decorator(user_authenticated, name='dispatch')
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
            available_seats = current_event.avlbl_seats
            price = current_event.ticket_price

            if ((no_of_tickets <= available_seats) & (available_seats > 0)):
                amount = no_of_tickets * price
                bookings = self.model(event=event, user=user, no_of_tickets=no_of_tickets, mobile_number=mobile_number,
                                      total=amount)
                bookings.save()

                current = available_seats - no_of_tickets
                current_event.avlbl_seats = current
                current_event.save()
                return redirect("success", id=id)
            else:
                return render(request, 'event/failed.html')


        else:
            events = Event.objects.get(id=kwargs['id'])
            form = self.form_class(initial={'event': events, 'user': request.user})
            self.context['form'] = form
            self.context['event'] = events
            return render(request, self.template_name, self.context)


@method_decorator(user_authenticated, name='dispatch')
class SuccessPage(TemplateView):
    model = EventBook
    template_name = 'event/succesfullBooking.html'
    context = {}

    def get(self, request, *args, **kwargs):
        id = kwargs.get('id')
        event = self.model.objects.get(id=id)
        self.context['event'] = event
        return render(request, self.template_name, self.context)


@method_decorator(user_authenticated, name='dispatch')
class Orders(TemplateView):
    model = EventBook
    template_name = 'event/orders.html'
    context = {}

    def get(self, request, *args, **kwargs):
        uname = request.user
        events = self.model.objects.all().filter(user=uname)
        self.context['events'] = events
        return render(request, self.template_name, self.context)


@method_decorator(user_authenticated, name='dispatch')
class OrderDetails(TemplateView):
    model = EventBook
    template_name = 'event/orderdetails.html'
    context = {}

    def get(self, request, *args, **kwargs):
        event = self.model.objects.get(id=kwargs['id'])
        self.context['event'] = event
        return render(request, self.template_name, self.context)


@method_decorator(no_amdin, name='dispatch')
@method_decorator(user_authenticated, name='dispatch')
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


@method_decorator(user_authenticated, name='dispatch')
@method_decorator(amdin_only, name='dispatch')
class ViewFeedBackAdmin(TemplateView):
    model = Feedback
    template_name = 'event/feebbackview.html'
    context = {}

    def get(self, request, *args, **kwargs):
        fbs = self.model.objects.all()
        self.context['fbs'] = fbs
        return render(request, self.template_name, self.context)


@method_decorator(user_authenticated, name='dispatch')
class SearchEvent(TemplateView):
    model = Event
    template_name = 'event/search.html'
    context = {}

    def get(self, request, *args, **kwargs):
        events = self.model.objects.all()
        eventfilter = EventFilter(request.GET, queryset=events)
        self.context['filter'] = eventfilter
        return render(request, self.template_name, self.context)


@method_decorator(user_authenticated, name='dispatch')
@method_decorator(amdin_only, name='dispatch')
class DailyCollection(TemplateView):
    form_class = DailyCollectionBydate
    template_name = 'event/dailycollection.html'
    context = {}

    def get(self, request, *args, **kwargs):
        # date=kwargs.get('date')
        form = self.form_class
        self.context['form'] = form
        # set=self.model.objects.filter(booking_date=date)
        # total = self.model.objects.filter(booking_date=date).aggregate(Sum('total'))
        # gtotal=total['total__sum']
        # self.context['total']=gtotal
        # self.context['set']=set
        # self.context['date']=date
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            date = form.cleaned_data.get('date')
            return redirect("amt", date=date)
        else:
            form = self.form_class
            self.context['form'] = form
            return render(request, self.template_name, self.context)


@method_decorator(user_authenticated, name='dispatch')
@method_decorator(amdin_only, name='dispatch')
class Amount(TemplateView):
    template_name = 'event/amountform.html'
    context = {}
    model = EventBook

    def get(self, request, *args, **kwargs):
        datestr = kwargs.get('date')
        date = parse_date(datestr)
        set = self.model.objects.filter(booking_date=date)
        total = self.model.objects.filter(booking_date=date).aggregate(Sum('total'))
        gtotal = total['total__sum']
        self.context['total'] = gtotal
        self.context['set'] = set
        print(set)
        print(gtotal)
        print(datestr)
        print(date)
        return render(request, self.template_name, self.context)


class DeleteFeedback(TemplateView):
    model = Feedback
    template_name = 'event/feebbackview.html'

    def get(self, request, *args, **kwargs):
        event = self.model.objects.get(id=kwargs["id"])
        event.delete()
        return redirect('viewfeedback')


def superuser_required(request):
    return render(request, 'event/superuser.html')


def login_required(request):
    return render(request, 'event/loginrequired.html')


def no_superuser(request):
    return render(request, 'event/no_superuser.html')
