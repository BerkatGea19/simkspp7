from django.db import models

# Create your models here.
class tpinjaman(models.Model):
    No_Rek_Pinjaman = models.CharField(primary_key=True, max_length=16)
    No_Rek_Tabungan = models.CharField(max_length=16)
    Jenis_Pinjaman = models.CharField(max_length=255)
    Kode_Anggota = models.CharField(max_length=7)
    Tanggal_Akad_Peminjaman = models.DateField()
    Prosentase_Bunga = models.CharField(max_length=255)
    Jumlah_Pinjaman = models.CharField(max_length=100)
    Biaya_Administrasi = models.CharField(max_length=50)
    Tabungan_Wajib = models.CharField(max_length=100)
    Jumlah_Angsuran = models.CharField(max_length=100)
    Angsuran_Perbulan = models.CharField(max_length=255)
    Bulan_Mulai_Angsuran = models.DateField()  
    Tanggal_Angsuran_Perbulan = models.DateField() 

    class Meta:
        db_table = "tblPinjaman"