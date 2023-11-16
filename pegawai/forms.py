from django import forms
from pegawai.models import mpegawai

class formpegawai(forms.ModelForm):
    class Meta:
        model = mpegawai
        fields = ['Kode_Petugas','Nama_Petugas']
        widgets = {'Kode_Petugas': forms.TextInput(attrs={'class': 'form-control'}),
                   'Nama_Petugas': forms.TextInput(attrs={'class': 'form-control'}),
                   }