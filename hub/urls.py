from django.urls import path
from . import views


urlpatterns = [
    path('',views.index_view,name='index'),
    path('notepad/',views.notepad_view, name='notepad'),
    path('create_member/',views.CreateMember.as_view(),name='create_member'),
    path('create_deposit/',views.CreateDeposit.as_view(),name='create_deposit'),
    path('create_payment/',views.CreateInternalPayment.as_view(),name='create_payment'),
    path('report/',views.report_view,name='report'),
    path('deposit_form/',views.deposit_form_view,name='deposit_form'),
    path('deposit_delete/<int:pk>/',views.DepositDeleteView.as_view(),name='deposit_delete'),
    path('internalpayment_delete/<int:pk>/',views.InternalPaymentDeleteView.as_view(),name='internalpayment_delete'),
    path('list_member/',views.ListMemberView.as_view(),name='list_member'),
    path('member_delete/<int:pk>/',views.MemberDeleteView.as_view(),name='member_delete'),
    path('delete_all_transactions/',views.delete_all_transactions,name='delete_all_transactions'),
    path('delete_all_members/',views.delete_all_members,name='delete_all_members'),
    path('export-excel/', views.ExportDeposit.as_view(), name='export-excel'),
]

app_name = 'hub'