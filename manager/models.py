from turtle import update
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class Manager(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE, related_name="manager")
    phone = models.CharField(max_length=17, null=True, unique=True)
    email = models.EmailField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user)


class BusStand(models.Model):
    manager = models.ForeignKey(Manager, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    capacity = models.PositiveIntegerField(blank=True, null=True)
    bus_total = models.IntegerField(null=True)
    revenue_total = models.FloatField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
 
    def __str__(self):
        return str(self.name)


class Payments(models.Model):
    CHOICES = (
        ('Paid', 'Paid'),
        ('Pending', 'Pending'),
        ('Not Paid', 'Not Paid'),
    )
    amount = models.FloatField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    phone = models.CharField(max_length=17, null=True)
    status = models.CharField(max_length=20, null=True, choices=CHOICES)
    plate_no = models.CharField(max_length=50, null=True, blank=True)
    customer_name = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return str(self.plate_no)