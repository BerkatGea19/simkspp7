from django.shortcuts import render

# Create your views here.
def anggota(request):
    anggota = {
        'nama': 'list anggota',
    }
    return render(request, 'anggota.html', anggota)