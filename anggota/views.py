from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import MAnggota
from django.contrib import messages

# Create your views here.
def anggota(request):
    anggota = {
        'nama': 'list anggota',
    }
    return render(request, 'tambah_anggota.html', anggota)

def tambah_anggota(request):
    return render(request, 'tambah_anggota.html')

def post_anggota(request):
    kdanggota = request.POST['kdanggota']
    nmAnggota = request.POST['nmAnggota']
    nik = request.POST['nik']
    tglLahir = request.POST['tglLahir']
    agama = request.POST['agama']
    no_hp = request.POST['no_hp']
    no_telprumah = request.POST['no_telprumah']
    pekerjaan = request.POST['pekerjaan']
    alamat = request.POST['alamat']
    email = request.POST['email']

    if MAnggota.objects.filter(kode_Anggota=kdanggota).exists():
         messages.error(request, 'NOMOR ANGGOTA SUDAH DIGUNAKAN!')
         return redirect(request.META.get('HTTP_REFERE','/'))
    else:  
        tambah_anggota=MAnggota(
            kode_Anggota=kdanggota,
            Nama_Anggota=nmAnggota,
            Nomor_Induk_Kependudukan=nik,
            Tgl_Lahir=tglLahir,
            Agama=agama,
            No_Hp=no_hp,
            No_Telp_Rumah=no_telprumah,
            Pekerjaan=pekerjaan,
            Alamat=alamat,
            Email=email,
        )
        tambah_anggota.save()
        messages.success(request, 'BERHASIL TAMBAH ANGGOTA')
    return HttpResponse("Data Anggota telah berhasil disimpan.")