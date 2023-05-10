from django.shortcuts import render,redirect
from django.views.generic import CreateView,DeleteView,ListView,View
from .models import Member,Deposit,InternalPayment
from django.urls import reverse_lazy,reverse
from django.db.models import Sum
from decimal import *
import numpy as np
from django import forms
from .forms import DepositForm
from django_excel import make_response_from_query_sets

# Create your views here.

def index_view(request):
    return render(request,'hub/index.html')

class CreateMember(CreateView):
    model = Member
    success_url = reverse_lazy('hub:list_member')
    fields = '__all__'

class CreateDeposit(CreateView):
    model = Deposit
    success_url = reverse_lazy('hub:report')
    fields = '__all__'

    class Meta:
        widgets = {
            'amount': forms.NumberInput(attrs={'class': 'form-floating mb-3'}),
        }

class CreateInternalPayment(CreateView):
    model = InternalPayment
    success_url = reverse_lazy('hub:report')
    fields = '__all__'

def report_view(request):
    # Get the models
    members = Member.objects.all()
    deposits = Deposit.objects.all()
    payments = InternalPayment.objects.all()

    #globals
    num_members = Decimal(members.count())
    sum_deposits = Decimal(deposits.aggregate(Sum('amount'))['amount__sum'] or 0)
    share_money = Decimal(sum_deposits * 1/num_members) 
    bank = {}
    owed_list = []
    answer_list = []
    # iterate through members to create the bank dictionary.
    for i in members:
        deposited = Decimal(deposits.filter(member=i.id).aggregate(Sum('amount'))['amount__sum'] or 0)
        paid_internally = Decimal(payments.filter(payer=i.id).aggregate(Sum('amount'))['amount__sum'] or 0)
        received = Decimal(payments.filter(recipient=i.id).aggregate(Sum('amount'))['amount__sum'] or 0)
        owes = share_money - (deposited + paid_internally) + received

        bank[i.name] = {
            'paid': deposited + paid_internally,
            'received': received,
            'owes': owes
        }

        owed_list.append([i.name,owes])
    # Create answer list
    # left = 0
    # right = len(owed_list) - 1
    
    owed_list.sort(key= lambda x: int(x[1]))
    # owed_list = list(map(lambda x: [x[0],round(x[1],2)],owed_list))
    counter = 0

    while len(owed_list) > 1:
        counter += 1
        owed_list.sort(key= lambda x: int(x[1]))


        left_person = owed_list[0][0]
        right_person = owed_list[-1][0]
        left_num = owed_list[0][1]
        right_num = owed_list[-1][1]
        message = f"{right_person} pays {left_person} ${round(right_num,2)}"
        message_two = f"{right_person} pays {left_person} ${round(abs(left_num),2)}"
        print(f"{counter}: {owed_list}")
        if left_num == 0:
            owed_list.pop(0)
        elif right_num == 0:
            owed_list.pop()
        elif abs(left_num) == abs(right_num):
            answer_list.append(message)
            owed_list.pop()
            owed_list.pop(0)
        elif abs(left_num) > abs(right_num):
            answer_list.append(message)
            owed_list[0][1] += Decimal(right_num)
            owed_list.pop()
        elif abs(right_num) > abs(left_num):
            answer_list.append(message_two)
            owed_list[-1][1] += Decimal(left_num)
            owed_list.pop(0)
        else:
            answer_list.append('error!')
            break

        

    context = {
        'members':members,
        'deposits':deposits,
        'payments':payments,
        'sum_deposits':sum_deposits,
        'share_money':share_money,
        'bank':bank,
        'owed_list':owed_list,
        'answer_list':answer_list,
    }

    return render(request,'hub/report.html',context=context)

def notepad_view(request):
    deposits = Deposit.objects.all()
    payments = InternalPayment.objects.all()
    joined_table = []

    for deposit in deposits:
        joined_table.append({'string':deposit,'time':deposit.time_added,'id':deposit.id,'type':'deposit'})
    for payment in payments:
        joined_table.append({'string':payment,'time':payment.time_added,'id':payment.id,'type':'payment'})

    joined_table = sorted(joined_table, key=lambda x: x['time'], reverse=True)




    context = {
        'joined_table':joined_table,
    }


    return render(request,'hub/notepad.html',context=context)

class DepositDeleteView(DeleteView):
    model = Deposit
    success_url = reverse_lazy('hub:notepad')
class InternalPaymentDeleteView(DeleteView):
    model = InternalPayment
    success_url = reverse_lazy('hub:notepad')
class MemberDeleteView(DeleteView):
    model = Member
    success_url = reverse_lazy('hub:list_member')

class ListMemberView(ListView):
    model = Member
    context_object_name = 'members'
    queryset = Member.objects.order_by('id')


def deposit_form_view(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = DepositForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            
            # Do code shit here🔻
            print(f"form:{form.cleaned_data}")
            # Save Form to Models
            # form.save()
            # redirect to a new URL:
            return redirect(reverse('hub:report'))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = DepositForm()
        # context = 

    return render(request,'hub/deposit_custom_form.html',context={'form':form})

def delete_all_transactions(request):
    Deposit.objects.all().delete()
    InternalPayment.objects.all().delete()
    return redirect (reverse('hub:notepad'))

def delete_all_members(request):
    Member.objects.all().delete()
    return redirect(reverse('hub:list_member'))

class ExportDeposit(View):
    def get(self, request):
        queryset = Deposit.objects.all()
        column_names = ['time_added', 'member','amount']
        filename = 'my_model.xlsx'
        return make_response_from_query_sets(queryset, column_names, filename, 'xlsx')