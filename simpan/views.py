from django.shortcuts import render, redirect
from .forms import formsimpan  # Perubahan pada nama formulir
from .models import mstabungan
from django.contrib import messages

def simpan(request):
    simpan = mstabungan.objects.all()
    return render(request, 'simpan/simpan.html',{'simpan':simpan})

def tambahsimpan_view(request):
    
    return render(request, 'simpan/indexsimpan.html')

def posttambah(request):
    nrt = request.POST['nrt']
    jt = request.POST['jt']
    ka = request.POST['ka']
    tpr = request.POST['tpr']
    jb = request.POST['jb']
    pb = request.POST['pb']
    sa = request.POST['sa']
    
    data_simpan = mstabungan(
        No_Rek_Tabungan=nrt,
        Jenis_Tabungan = jt,
        Kode_Anggota = ka,
        Tanggal_Pembukaan_Rekening = tpr,
        Jenis_Bunga = jb,
        Prosentase_Bunga = pb,
        Status_Aktif=sa
    )

    data_simpan.save()
    return redirect('simpan')
def edit(request, No_Rek_Tabungan):
    data_simpanan = mstabungan.objects.get(No_Rek_Tabungan=No_Rek_Tabungan)
    context = {
        'data_simpan': data_simpanan
    }
    return render(request, 'simpan/edit.html', context)

def update(request):
   nrt = request.POST['nrt']
   jt = request.POST['jt']
   ka = request.POST['ka']
   tpr = request.POST['tpr']
   jb = request.POST['jb']
   pb = request.POST['pb']
   sa = request.POST['sa']

   data_simpanan =mstabungan.objects.get(No_Rek_Tabungan=nrt)
   data_simpanan.Jenis_Tabungan=jt
   data_simpanan.Kode_Anggota=ka
   data_simpanan.Tanggal_Pembukaan_Rekening=tpr
   data_simpanan.Jenis_Bunga=jb
   data_simpanan.Prosentase_Bunga=pb
   data_simpanan.Status_Aktif=sa
   data_simpanan.save()
   messages.success(request, 'BERHASIL UPDATE ANGGOTA')
   return redirect('simpan')

def destroy(request,No_Rek_Tabungan):
    simpanan =mstabungan.objects.get(No_Rek_Tabungan=No_Rek_Tabungan).delete()
    messages.success(request, 'BERHASIL HAPUS DATA')
    return redirect('simpan')