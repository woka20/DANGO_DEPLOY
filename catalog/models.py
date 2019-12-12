from django.db import models

# Create your models here.

class Produk(models.Model):
    gambar=models.CharField(max_length=300)
    nama=models.CharField(max_length=300)
    harga=models.DecimalField(max_digits=30, decimal_places=2)

    def __str__(self):
        return self.nama

class Deskripsi(models.Model):
    nama=models.ForeignKey(Produk, on_delete=models.CASCADE)
    deskripsi=models.CharField(max_length=200)

    def __str__(self):
        return self.deskripsi


