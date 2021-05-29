from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import EventCategory,Event
from .forms import EventCategoryForm,EventCreationFrom
# Create your views here.

def show_hipe(request):
    return render(request,"event/base.html")

class EventCategoryView(TemplateView):
    model=EventCategory
    form_class=EventCategoryForm
    template_name = 'event/event_category.html'
    context={}
    def get(self, request, *args, **kwargs):
        events=self.model.objects.all()
        self.context["events"]=events
        self.context["form"]=self.form_class
        return render(request,self.template_name,self.context)
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
    model=EventCategory
    form_class=EventCategoryForm
    template_name = "event/event_category.html"
    context={}
    def get(self, request, *args, **kwargs):
        brand=self.model.objects.get(id=kwargs["id"])
        form=self.form_class(instance=brand)
        self.context["form"]=form
        return render(request,self.template_name,self.context)
    def post(self, request, *args, **kwargs):
        event = self.model.objects.get(id=kwargs["id"])
        form = self.form_class(request.POST,instance=event)
        if form.is_valid():
            form.save()
            return redirect("category")
        else:
            self.context["form"]=form
            return render(request, self.template_name, self.context)

class EventDelete(TemplateView):
    model=EventCategory
    form_class=EventCategoryForm
    template_name = "event/event_category.html"
    context = {}
    def get(self, request, *args, **kwargs):
        event=self.model.objects.get(id=kwargs["id"])
        event.delete()
        return redirect("category")

class EventCreationView(TemplateView):
    model=Event
    form_class=EventCreationFrom
    template_name = 'event/eventcreation.html'
    context={}
    def get(self, request, *args, **kwargs):
        form =self.form_class
        self.context['form']=form
        return render(request,self.template_name,self.context)
    def post(self, request, *args, **kwargs):
        form=self.form_class(request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect("eventcreation")
        else:
            self.context['form']=form
            return render(request,self.template_name,self.context)

