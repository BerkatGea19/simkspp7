from django.shortcuts import render

# Create your views here.
def contact(request):
    contact = {
        'name':'Kontak kami'
    }
    return render(request, 'contact.html', contact)