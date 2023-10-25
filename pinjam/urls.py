from django.urls import path
from . import views

urlpatterns = [
    path('', views.pinjam, name="pinjam"),
]