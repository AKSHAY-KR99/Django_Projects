from django.shortcuts import render, redirect
from event.models import EventCategory, Event, EventBook
from event.forms import EventCategoryForm, EventCreationFrom, UserRegistrationForm, EventBookingForm
from django.views.generic import TemplateView
from django.contrib.auth import login, authenticate, logout


# Create your views here.
def show_hipe(request):
    return render(request, "event/base.html")


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


class EventEdit(TemplateView):
    model = EventCategory
    form_class = EventCategoryForm
    template_name = "event/event_category.html"
    context = {}

    def get(self, request, *args, **kwargs):
        brand = self.model.objects.get(id=kwargs["id"])
        form = self.form_class(instance=brand)
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


class EventDelete(TemplateView):
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


class ViewEventDetails(TemplateView):
    model = Event
    template_name = 'event/view_details.html'
    context = {}

    def get(self, request, *args, **kwargs):
        event = self.model.objects.get(id=kwargs["id"])
        self.context['event'] = event
        return render(request, self.template_name, self.context)


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
    model = Event
    form_class = EventBookingForm
    template_name = 'event/event_booking.html'
    context = {}

    def get(self, request, *args, **kwargs):
        event = self.model.objects.get(id=kwargs['id'])
        self.context['event'] = event
        form = self.form_class(initial={"event": event, "user": request.user})
        self.context['form'] = form
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        id = kwargs['id']
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect("success", id=id)
        else:
            print("rorrrrrrrrrrrssszzzz")


class SuccessPage(TemplateView):
    model = EventBook
    template_name = 'event/succesfullBooking.html'
    context = {}

    def get(self, request, *args, **kwargs):
        id = kwargs.get('id')
        event = self.model.objects.get(id=id)
        total = (event.number_of_tickets) * (event.event.ticket_price)
        self.context['event'] = event
        self.context['total'] = total
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
