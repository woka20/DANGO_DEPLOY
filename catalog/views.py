from django.shortcuts import render, redirect
from .models import Produk, Deskripsi
# Create your views here.

def home(request):
    produk=Produk.objects.all()
    return render(request, 'catalog/index.html', {'produks':produk})

def form(request):
    return render(request,'catalog/form.html')

def submit(request):
    # list_desc=Deskripsi.objects.filter(nama=produk_id).all()
    barang=Produk(
        gambar=request.POST['gambar_post'],
        nama=request.POST['nama_post'],
        harga=request.POST['harga_post']
    )
    barang.save()
    desc=Deskripsi(
        nama=request.POST['gambar_post'],
        deskripsi=request.POST['list_barang']
    )
    desc.save()
    return render(request,'catalog/index.html')

def detail(request, produk_id):
    full_produk=Produk.objects.get(id=produk_id)
    list_item=Deskripsi.objects.filter(id=produk_id).all()
    

    return render(request, 'catalog/detail.html', {'daftar': list_item})


