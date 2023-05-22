from django.db import models
from django.utils import timezone

# Create your models here.
class BukuTamu(models.Model):  
  nama = models.TextField(max_length=50)
  perusahaan = models.TextField(max_length=100)
  jumlah_tamu = models.IntegerField()
  tgl_awal = models.DateField(null=True, blank=True)
  tgl_akhir = models.DateField(null=True, blank=True)
  tujuan = models.TextField(max_length=100)
  keperluan = models.TextField(max_length=200)
  create_date = models.DateTimeField(auto_now_add=True)

  class Meta:    
    verbose_name = 'bukutamu'
    verbose_name_plural = 'bukutamus'

  def __str__(self):    
    return self.nama
