
from .models import Event
from django.shortcuts import  HttpResponseRedirect, render, redirect

from Events.forms import EventModelForm, TicketModelForm, UserCreationForm, Book_Ticket


#User Landing Page
def landing_page(request):
    return render(request, 'landing_page.html')

#User Home Page
def home_page(request):
    return render(request,'home_page.html')

#User About Page
def about_page(request):
    return render(request,'about_page.html')

#User Contact Page  
def contact_page(request):
    return render(request,'contact_page.html')

def login(request):
     form = UserCreationForm()    
     if request.method =="POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home_page.html")
     context ={
        "form": form
    }
     return render(request, 'Registration/login.html', context)


def signup(request):
    form = UserCreationForm()    
    if request.method =="POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("Registration/login.html")
    context ={
        "form": form
    }
    return render(request, 'Registration/signup.html', context)


def event_list(request):
    Events = Event.objects.all()
    context ={
        "Events":Events
    }
    return render(request, 'Events/event_list.html', context)


def event_detail(request, pk):
    event = Event.objects.get(id=pk)
    event.time = event.time.strftime('%H:%M:%S')
    context = {
       "Event":event
    }
    return render(request, 'Events/event_detail.html', context)


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


def update_event(request, pk):
    context ={}
    event = Event.objects.get(id=pk)
    form = EventModelForm(request.POST or None, instance = event)

    # save the data from the form and
    # redirect to detail_view
  
    if form.is_valid():
        form.save()
        return redirect("Events:event-list"+pk)
    context["form"] = form
    return render(request, "Events/update_event.html", context)

    #   form = EventModelForm(instance=Event)
    #   if request.method =="POST":
    #     form = EventModelForm(request.POST, instance=Event)
    #     if form.is_valid():
    #         form.save()
    #         return redirect("Events:event-list"+pk) 
    #   context = {
    #     "form": form,
    #     "Events": event       
    # } 
    #   return render(request, "Events/update_event.html", context) 


def event_delete(request,pk):
    context ={}
    event = Event.objects.get(id=pk)
    if request.method =="POST":
            event.delete()
            return redirect("Events:event-list")
    return render(request, 'Events/event_delete.html',context)
   

# Admin Page

def admin_login(request):
    return render(request,'admin_login.html')

#Admin View Bookings

def admin_booking(request):
    if request.session:
        booking = Book_Ticket.objects.all()
        data = {'booking':booking}
        return render(request,'admin_booking.html',context=data)
    else:
        data = {'status':'You need to login first'}
        return render(request,'admin_login.html',context=data)

def admin_home(request):
    return render(request,'admin_home.html')




