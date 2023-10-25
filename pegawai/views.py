from django.shortcuts import render

# Create your views here.
def pegawai(request):
    pegawai = {
        'nama': 'list pegawai',
    }
    return render(request, 'pegawai.html', pegawai)