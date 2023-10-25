from django.urls import path
from . import views

urlpatterns = [
    path('', views.simpan, name="simpan"),
]