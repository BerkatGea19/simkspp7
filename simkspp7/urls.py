
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('about.urls')),
    path('blog/', include('blog.urls')),
    path('contact/', include('contact.urls')),
    path('login/',include('login.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('pegawai/', include('pegawai.urls')),
    path('anggota/', include('anggota.urls')),
    path('pinjam/', include('pinjam.urls')),
    path('simpan/', include('simpan.urls')),
]
