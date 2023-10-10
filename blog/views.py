from django.shortcuts import render

# Create your views here.
def blog(request):
    context = {
        'name':'About Us',
    }
    return render(request, 'blog.html', context)