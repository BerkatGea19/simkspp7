from django.shortcuts import render, redirect
from pegawai.forms import formpegawai
from pegawai.models import mpegawai
from django.contrib import messages

# Create your views here.
def tambahpegawai(request):
    if request.method == "POST":
        form =formpegawai(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('pegawai')
            except:
                pass
    else:
        form = formpegawai()
    return render(request, 'indexpegawai.html',{'form':form})

def pegawai(request):
    pegawai = mpegawai.objects.all()
    return render(request, "pegawai.html",{'pegawai':pegawai})

def edit(request, Kode_Petugas):
    data_petugas = mpegawai.objects.filter(Kode_Petugas=Kode_Petugas)
    context = {
        'data_petugas':data_petugas
    }
    return render(request, 'edit.html', context)
    # pegawai = mpegawai.objects.get(Kode_Petugas=Kode_Petugas)
    # return render(request, 'edit.html', {'pegawai1':pegawai})

def update(request):
   Nama_Petugas = request.POST['Nama_Petugas']
   Kode_Petugas = request.POST['Kode_Petugas']

   data_petugas =mpegawai.objects.get(Kode_Petugas=Kode_Petugas)
   data_petugas.Nama_Petugas=Nama_Petugas
   data_petugas.save()
   messages.success(request, 'BERHASIL UPDATE ANGGOTA')
   return redirect('pegawai')

def destroy(request,Kode_Petugas):
    pegawai =mpegawai.objects.get(Kode_Petugas=Kode_Petugas).delete()
    messages.success(request, 'BERHASIL HAPUS DATA')
    return redirect('pegawai')
