from django.urls import path
from . import views


urlpatterns = [
    path('', views.anggota, name="anggota"),
    path('tambah_anggota', views.tambah_anggota,name="tambahAnggota"),
    path('post_anggota', views.post_anggota, name="postanggota"),
    path('master_anggota',views.master_anggota, name='masteranggota'),
    path('update_anggota/<str:kode_Anggota>/', views.update_anggota, name='update_anggota'),
    path('postupdate_anggota/', views.postupdate_anggota, name="postUpdateAnggota"),
]  