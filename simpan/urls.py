# urls.py
from django.urls import path
from .views import *  # tambahkan import delete

urlpatterns = [
    path('', simpan, name="simpan"),
    path('tambahsimpan/', tambahsimpan_view, name='tambahsimpan'),
    path('posttambah', posttambah, name='posttambah'),
    path('edit/<str:No_Rek_Tabungan>/', edit, name='edit'),
    path('update', update, name='update'),
    path('delete/<str:No_Rek_Tabungan>/', destroy, name='destroy'),  # tambahkan path untuk delete
]
