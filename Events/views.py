from .models import Event
from django.shortcuts import render, redirect

from Events.forms import EventModelForm, TicketModelForm

def home_page(request):
    return render(request,'home_page.html')

def landing_page(request):
    return render(request, 'landing_page.html')

def login_page(request):
    return render(request, 'registration/login.html')

def event_list(request):
    Events = Event.objects.all()
    context ={
        "Events":Events
    }
    return render(request, 'Events/event_list.html', context)


def create_event(request):
    form = EventModelForm()
    if request.method =="POST":
        form = EventModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("Events:event-list")
    context ={
        "form": form
    }
    return render(request, 'Events/create_event.html', context)

def book_ticket(request):
    form = TicketModelForm()    
    if request.method =="POST":
        form = TicketModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("Events:event-list")
    context ={
        "form": form
    }
    return render(request, 'Events/book_ticket.html', context)

def update_event(request):
    form = EventModelForm()
    if request.method =="POST":
        form = EventModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("Events:event-list")
    context ={
        "form": form
    }
    return render(request, 'Events/update_event.html', context)

def event_detail(request, pk):
    event = Event.objects.get(id=pk)
    context = {
       "Event":event
    }
    return render(request, 'Events/event_detail.html', context)


def about_page(request):
    return render(request,'pages/about_page.html')

    
def contact_page(request):
    return render(request, 'pages/contact_page.html')

   











