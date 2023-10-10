from django.shortcuts import render

# Create your views here.
def index(request):
	context = {
		'name':'SIM Koperasi Simpan Pinjam',
	}
	return render(request, 'index.html', context)