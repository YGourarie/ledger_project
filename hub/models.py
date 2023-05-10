from django.db import models
from datetime import datetime

# Create your models here.

class Member(models.Model):
    time_added = models.DateTimeField(auto_now_add=True, null=True,blank=True)
    name = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.name}"


# Time format: self.time_added.strftime('%Y-%m-%d %H:%M')
class Deposit(models.Model):
    time_added = models.DateTimeField(auto_now_add=True, null=True,blank=True)
    member = models.ForeignKey(Member,on_delete=models.CASCADE,null=True)
    amount = models.IntegerField()

    def __str__(self):
        return f"{self.member} deposited ${self.amount}"


class InternalPayment(models.Model):
    time_added = models.DateTimeField(auto_now_add=True, null=True,blank=True)
    payer = models.ForeignKey(Member,on_delete=models.SET_NULL,null=True,related_name='payer')
    recipient = models.ForeignKey(Member,on_delete=models.SET_NULL,null=True,related_name='recipient')
    amount = models.IntegerField()

    def __str__(self):
        return f"{self.payer} paid {self.recipient} ${self.amount}"


