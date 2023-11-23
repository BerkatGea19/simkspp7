from django import forms
from .models import mstabungan

class formsimpan(forms.ModelForm):
    class Meta:
        model = mstabungan
        fields = [
            'No_Rek_Tabungan', 'Jenis_Tabungan', 'Kode_Anggota',
            'Tanggal_Pembukaan_Rekening', 'Jenis_Bunga', 'Prosentase_Bunga', 'Status_Aktif'
        ]

    JENIS_TABUNGAN_CHOICES = [
        ('Simpanan_Wajib', 'Simpanan Wajib'),
        ('Simpanan_Pokok', 'Simpanan Pokok'),
    ]

    JENIS_BUNGA_CHOICES = [
        ('bungaFlat', 'Bunga Flat'),
        ('bungaMenurun', 'Bunga Menurun'),
        ('bungaMenurunEfektif', 'Bunga Menurun Efektif',)
    ]

    STATUS_AKTIF_CHOICES = [
        ('aktif', 'Aktif'),
        ('nonaktif', 'Nonaktif'),
    ]

    widgets = {
        'No_Rek_Tabungan': forms.TextInput(attrs={'class': 'form-control'}),
        'Jenis_Tabungan': forms.Select(choices=JENIS_TABUNGAN_CHOICES, attrs={'class': 'form-control'}),
        'Kode_Anggota': forms.TextInput(attrs={'class': 'form-control'}),
        'Tanggal_Pembukaan_Rekening': forms.DateInput(attrs={'type': 'date', 'class': 'form-control', 'autocomplete': 'off'}),
        'Jenis_Bunga': forms.Select(choices=JENIS_BUNGA_CHOICES, attrs={'class': 'form-control'}),
        'Prosentase_Bunga': forms.TextInput(attrs={'class': 'form-control'}),
        'Status_Aktif': forms.Select(choices=STATUS_AKTIF_CHOICES, attrs={'class': 'form-control'}),
    }

    input_formats = ['%Y-%m-%d']  # Sesuaikan format dengan yang diinginkan
