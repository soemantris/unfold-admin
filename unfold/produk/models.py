from django.db import models
import uuid
from django.contrib.auth.models import User
# Create your models here.
class Barang(models.Model):
    nama = models.CharField(max_length=200)
    deskripsi = models.TextField()
    harga = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    image = models.ImageField(upload_to='produk/', blank=True, null=True)

    @property
    def in_stock(self):
        return self.stock > 0

    def __str__(self):
        return self.nama
        
class Pesanan(models.Model):
    class StatusChoices(models.TextChoices):
        TUNDA = 'Tunda'
        KONFIRMASI = 'Konfirmasi'
        BATAL = 'Batal'

    pesanan_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tgl_pesanan = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=10,
        choices=StatusChoices.choices,
        default=StatusChoices.TUNDA
    )

    jum_barang = models.ManyToManyField(
        Barang, through="Pembelian", related_name='orders')

    def __str__(self):
        return f"Pesanan {self.pesanan_id} oleh {self.user.username}"

class Pembelian(models.Model):
    pesans = models.ForeignKey(Pesanan, on_delete=models.CASCADE, verbose_name='Pesanan')
    barangs = models.ForeignKey(Barang, on_delete=models.CASCADE, verbose_name='Nama Barang')
    quantity = models.PositiveIntegerField()

    @property
    def total_harga(self):
        return self.barangs.harga * self.quantity

    def __str__(self):
        return f"{self.quantity} x {self.barangs.nama} in Order {self.pesans.pesanan_id}"