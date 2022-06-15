from django.contrib import admin
from .models import *


class ManagerAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'email', 'image')


class BusStandAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'capacity')


class PaymentsAdmin(admin.ModelAdmin):
    list_display = ('plate_no', 'amount', 'phone', 'status', 'customer_name')


admin.site.register(Manager, ManagerAdmin)
admin.site.register(BusStand, BusStandAdmin)
admin.site.register(Payments, PaymentsAdmin)
