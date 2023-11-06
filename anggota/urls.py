from django.urls import path
from . import views


urlpatterns = [
    path('', views.anggota, name="anggota"),
    path('tambah_anggota', views.tambah_anggota,name="tambahAnggota"),
    path('post_anggota', views.post_anggota, name="postanggota")
]  