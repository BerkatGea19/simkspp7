# Generated by Django 4.2.5 on 2023-11-06 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='mpegawai',
            fields=[
                ('Kode_Petugas', models.CharField(max_length=7, primary_key=True, serialize=False)),
                ('Nama_Petugas', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'tblpegawai',
            },
        ),
    ]
