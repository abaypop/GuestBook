from django.contrib import admin
from .models import *

# Register your models here.
class BukuTamuAdmin(admin.ModelAdmin):  
  list_display = ['nama', 'perusahaan', 'jumlah_tamu', 'tgl_awal', 'tgl_akhir', 'tujuan', 'keperluan', 'create_date']  
  list_filter = ['create_date']

admin.site.register(BukuTamu, BukuTamuAdmin)