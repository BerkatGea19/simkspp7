from django.shortcuts import render

# Create your views here.
def simpan(request):
    simpan = {
        'nama': 'data simpan',
    }
    return render(request, 'simpan.html', simpan)