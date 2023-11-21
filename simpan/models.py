from django.db import models

# Create your models here.

class mstabungan(models.Model):
    No_Rek_Tabungan = models.CharField(primary_key=True, max_length=16)
    Jenis_Tabungan = models.CharField(max_length=14)
    Kode_Anggota = models.CharField(max_length=7)
    Tanggal_Pembukaan_Rekening = models.DateField()
    Jenis_Bunga = models.CharField(max_length=255)  
    Prosentase_Bunga = models.CharField(max_length=255)  
    Status_Aktif = models.CharField(max_length=255)  

    class Meta:
        db_table = "MasterTabungan"