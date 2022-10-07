from django.contrib import admin
from .models import Admin, Book_Ticket, User, Event

# Register your models here.
admin.site.register(Admin)
admin.site.register(User)
admin.site.register(Event)
admin.site.register(Book_Ticket)



