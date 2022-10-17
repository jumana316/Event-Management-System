
from django.db import models

class User(models.Model):
    name = models.CharField(max_length=20, unique=True)
    email = models.CharField(max_length=40)
    gender = models.CharField(max_length=6)
    password = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name}"

class Admin(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=40)
    password = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.name}"

class Event(models.Model):
    name = models.CharField(max_length=20)
    time = models.TimeField()
    date = models.DateField()
    duration = models.PositiveIntegerField()
    description = models.CharField(max_length=50)
    coordinator = models.CharField(max_length=20)
    max_participants = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name}"

class Book_Ticket(models.Model):
    first_name = models.CharField(max_length=20,)
    last_name = models.CharField(max_length=20)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    phone = models.PositiveBigIntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


    


