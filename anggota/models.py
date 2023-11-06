from django.db import models

class MAnggota(models.Model):
    kode_Anggota = models.CharField(primary_key=True, max_length=7)
    Nama_Anggota = models.CharField(max_length=255)
    Nomor_Induk_Kependudukan = models.CharField(max_length=16)
    Tgl_Lahir = models.DateField()
    Agama = models.CharField(max_length=15)
    No_Hp = models.CharField(max_length=12)
    No_Telp_Rumah = models.CharField(max_length=12)
    Pekerjaan = models.CharField(max_length=255)
    Alamat = models.CharField(max_length=552)
    Email = models.EmailField()
