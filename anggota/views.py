from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse
from .models import MAnggota
from django.contrib import messages
import json
from django.core.serializers import serialize
from django.db.models.query import QuerySet
from django.core.serializers.json import DjangoJSONEncoder

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
         return redirect(request.META.get('HTTP_REFERER','/'))
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

def master_anggota(request):
    data_anggota = MAnggota.objects.all().order_by('-kode_Anggota')
    # # Serialize the queryset into JSON
    # serialized_data = serialize('json', data_anggota)
    
    # # Convert the serialized data to a Python list
    # data_list = json.loads(serialized_data)

    # # Convert date fields to string format
    # for entry in data_list:
    #     fields = entry['fields']
    #     fields['Tgl_Lahir'] = fields['Tgl_Lahir']  # format the date as needed

    # return JsonResponse(data_list, safe=False, encoder=DjangoJSONEncoder)
    context = {
        'data_anggota' : data_anggota
    }
    return render(request, 'master-anggota.html', context)

def update_anggota(request,kode_Anggota):
    data_anggota = MAnggota.objects.get(kode_Anggota=kode_Anggota)
    context = {
        'data_anggota':data_anggota
    }
    return render(request, 'update-anggota.html', context)

def postupdate_anggota(request):
    kode_Anggota = request.POST['kdanggota']
    Nama_Anggota = request.POST['Nama_Anggota']
    Nomor_Induk_Kependudukan = request.POST['Nomor_Induk_Kependudukan']
    Tgl_Lahir = request.POST['Tgl_Lahir']
    Agama = request.POST['Agama']
    No_Hp = request.POST['No_Hp']
    No_Telp_Rumah = request.POST['No_Telp_Rumah']
    Pekerjaan = request.POST['Pekerjaan']
    Alamat = request.POST['Alamat']
    Email = request.POST['Email']

    anggota =MAnggota.objects.get(kode_Anggota=kode_Anggota)
    return redirect(request.META.get('HTTP_REFERER', '/'))