from django.db import models

# Create your models here.
class mpegawai(models.Model):
    Kode_Petugas = models.CharField(primary_key=True, max_length=7)
    Nama_Petugas = models.CharField(max_length=100)

    class Meta:
        db_table="tblpegawai"  