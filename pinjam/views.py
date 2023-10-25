from django.shortcuts import render

# Create your views here.
def pinjam(request):
    pinjam = {
        'nama': 'list pinjam',
    }
    return render(request, 'pinjam.html', pinjam)