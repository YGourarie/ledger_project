from django.contrib import admin
from .models import Member,Deposit,InternalPayment

# Register your models here.

admin.site.register(Member)
admin.site.register(Deposit)
admin.site.register(InternalPayment)