
from django import forms
from django.forms import DateInput, EmailInput, NumberInput, PasswordInput, Select, TextInput, TimeInput
from .models import Admin, Event, Book_Ticket, User

class EventModelForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name','time','date','duration','description','coordinator','max_participants']
        widgets = {
            'name':TextInput(attrs={'class': "form-control",'style': 'max-width: 300px;','placeholder': 'Name'}),
            'time':TimeInput(attrs={'class': "form-control",'style': 'max-width: 300px;','placeholder': 'Time'}),
            'date':DateInput(attrs={'class': "form-control",'style': 'max-width: 300px;','placeholder': 'Date'}),
            'duration':NumberInput(attrs={'class': "form-control",'style': 'max-width: 300px;','placeholder': 'Duration'}),
            'description':TextInput(attrs={'class': "form-control",'style': 'max-width: 300px;','placeholder': 'Description'}),
            'coordinator':TextInput(attrs={'class': "form-control",'style': 'max-width: 300px;','placeholder': 'Coordinator'}),
            'max_participants':NumberInput(attrs={'class': "form-control",'style': 'max-width: 300px;','placeholder': 'Max_Participants'}),        
        }

class TicketModelForm(forms.ModelForm):
    class Meta:
        model = Book_Ticket
        fields = ['first_name', 'last_name', 'event','phone']
        widgets = {
            'first_name':TextInput(attrs={'class': "form-control",'style': 'max-width: 300px;','placeholder': 'First Name'}),
            'last_name':TextInput(attrs={'class': "form-control",'style': 'max-width: 300px;','placeholder': 'Last Name'}),
            'event':Select(attrs={'class': "form-control",'style': 'max-width: 300px;','placeholder': 'Event'}),
            'phone':NumberInput(attrs={'class': "form-control",'style': 'max-width: 300px;','placeholder': 'Number'})
        }

class UserCreationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name','email','gender','password']
        widgets = {
            'name':TextInput(attrs={'class': "form-control",'style': 'max-width: 300px;','placeholder': 'Name'}),
            'email':EmailInput(attrs={'class': "form-control",'style': 'max-width: 300px;','placeholder': 'Mail'}),
            'gender':Select(attrs={'class': "form-control",'style': 'max-width: 300px;','placeholder': 'Gender'}),
            'password':PasswordInput(attrs={'class': "form-control",'style': 'max-width: 300px;','placeholder': 'Enter Password'}),
        }

class AdminCreationForm(forms.ModelForm):
    class Meta:
        model:Admin
        fields = ['name','email','password']
        widgets = {
            'name':TextInput(attrs={'class': "form-control",'style': 'max-width: 300px;','placeholder': 'Name'}),
            'email':EmailInput(attrs={'class': "form-control",'style': 'max-width: 300px;','placeholder': 'Mail'}),
            'password':PasswordInput(attrs={'class': "form-control",'style': 'max-width: 300px;','placeholder': 'Enter Password'})

        }


