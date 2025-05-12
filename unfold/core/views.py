from django.shortcuts import render

# Create your views here.
from produk.models import Barang, Pesanan, Pembelian
# mengisikan queryset ke context


def dashboard_callback(request, context):
    # queryset dari models
    hitung_barang = Barang.objects.count()
    tgl_barang = Barang.objects.all()
    hitung_pesanan = Pesanan.objects.count()
    hitung_beli = Pembelian.objects.count()
    tbl_beli = Pembelian.objects.all()
    context.update({
        "hitung_barang": hitung_barang,
        "hitung_pesanan": hitung_pesanan,
        "hitung_beli": hitung_beli,
        "tbl_barang": tgl_barang,
        "tbl_beli": tbl_beli,
    })

    return context
def index(request):
    return render(request, 'index.html')