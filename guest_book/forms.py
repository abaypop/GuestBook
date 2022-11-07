from django import forms
from .models import BukuTamu

#class BukuTamuForm(forms.Form):
#    nama = forms.CharField(required=True, max_length=50, widget=forms.TextInput(attrs={'class':'form-control', 'id':'nama', 'placeholder': 'Nama'}))
#    perusahaan = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'id':'perusahaan', 'placeholder': 'Perusahaan/Instansi/Personal'}))
#    jumlah_tamu = forms.IntegerField(required=True, min_value=1, widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder': 'Jumlah Tamu'}))
#    tujuan = forms.CharField(required=True, max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Bagian/Personal Tujuan'}))
#    keperluan = forms.CharField(required=True, max_length=100, widget=forms.Textarea(attrs={'class':'form-control', 'placeholder': 'Keperluan', 'row':3 })) 

class BukuTamuForm(forms.ModelForm):
  class Meta:
    model = BukuTamu
    fields = ('nama','perusahaan','jumlah_tamu','tujuan','keperluan')
    widgets = {
      'nama': forms.TextInput(attrs={'class': 'form-control', 'id':'nama', 'placeholder':'Nama'}),
      'perusahaan': forms.TextInput(attrs={'class': 'form-control', 'id':'perusahaan', 'placeholder':'Perusahaan'}),
      'jumlah_tamu': forms.NumberInput(attrs={'class': 'form-control', 'id':'jumlah_tamu', 'placeholder':'Jumlah Tamu'}),
      'tujuan': forms.TextInput(attrs={'class': 'form-control', 'id':'tujuan', 'placeholder':'Tujuan'}),
      'keperluan': forms.Textarea(attrs={'class': 'form-control', 'id':'keperluan', 'placeholder':'Keperluan'})
    }   