from django import forms
from .models import BukuTamu
import datetime

class BukuTamuForm(forms.ModelForm):    
  class Meta:
    model = BukuTamu
    fields = ('nama','perusahaan','jumlah_tamu','tgl_awal','tgl_akhir','tujuan','keperluan')  
    widgets = {
      'nama': forms.TextInput(
        attrs={'class': 'form-control', 'id':'nama', 'placeholder':'Nama', 'autocomplete': 'off'}
        ),
      'perusahaan': forms.TextInput(
        attrs={'class': 'form-control', 'id':'perusahaan', 'placeholder':'Perusahaan', 'autocomplete': 'off'}
        ),
      'jumlah_tamu': forms.NumberInput(
        attrs={'class': 'form-control', 'id':'jumlah_tamu', 'placeholder':'Jumlah Tamu', 'min':1}
        ),
      'tgl_awal': forms.DateInput(        
        attrs={'class': 'form-control', 'type': 'date', 'id': 'tgl_awal', 'placeholder':'Dari Tanggal', 'value': datetime.date.today}
        ),
      'tgl_akhir': forms.DateInput(
        attrs={'class': 'form-control', 'type': 'date', 'id':'tgl_akhir', 'placeholder':'Hingga Tanggal', 'value': datetime.date.today}
        ),
      'tujuan': forms.TextInput(
        attrs={'class': 'form-control', 'id':'tujuan', 'placeholder':'Tujuan'}
        ),
      'keperluan': forms.Textarea(
        attrs={'class': 'form-control', 'id':'keperluan', 'placeholder':'Keperluan'}
        )
    }   