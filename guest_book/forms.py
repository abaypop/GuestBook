from django import forms
from .models import BukuTamu
from django.utils.translation import gettext as _

class BukuTamuForm(forms.ModelForm):        
  class Meta:
    model = BukuTamu
    fields = ('nama','perusahaan','jumlah_tamu','tujuan','keperluan')    
    widgets = {
      'nama': forms.TextInput(        
        attrs={'class': 'form-control', 'id':'nama', 'placeholder':'Nama', 'autocomplete': 'off',
               'oninvalid':'this.setCustomValidity("Masukkan nama")',
               'oninput': 'this.setCustomValidity("")'}
        ),
      'perusahaan': forms.TextInput(
        attrs={'class': 'form-control', 'id':'perusahaan', 'placeholder':'Perusahaan', 'autocomplete': 'off',
               'oninvalid':'this.setCustomValidity("Masukkan asal instansi/perusahaan")',
               'oninput': 'this.setCustomValidity("")'}
        ),
      'jumlah_tamu': forms.NumberInput(        
        attrs={'class': 'form-control', 'id':'jumlah_tamu', 'placeholder':'Jumlah Tamu', 'min':1,
               'oninvalid':'this.setCustomValidity("Masukkan jumlah tamu")',
               'oninput': 'this.setCustomValidity("")'}
        ),      
      'tujuan': forms.TextInput(
        attrs={'class': 'form-control', 'id':'tujuan', 'placeholder':'Tujuan',
               'oninvalid':'this.setCustomValidity("Masukkan bagian/nama tujuan")',
               'oninput': 'this.setCustomValidity("")'}
        ),
      'keperluan': forms.Textarea(
        attrs={'class': 'form-control', 'id':'keperluan', 'placeholder':'Keperluan',
               'oninvalid':'this.setCustomValidity("Masukkan keperluan anda")',
               'oninput': 'this.setCustomValidity("")'}
        )
    }              