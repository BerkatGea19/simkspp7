from django.urls import path
from . import views

urlpatterns = [
    path('', views.pegawai, name="pegawai"),
    path('tambahpegawai', views.tambahpegawai, name='tambahpegawai'),
    path('edit/<str:Kode_Petugas>', views.edit, name='edit'),
    path('update', views.update, name='update'),
    path('delete/<str:Kode_Petugas>', views.destroy, name='destroy')
]