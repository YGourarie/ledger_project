from django import forms

class DepositForm(forms.Form):
    member = forms.CharField(label='Member')
    amount = forms.IntegerField(label='Amount')