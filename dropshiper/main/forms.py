from django import forms

class KonsumenForm(forms.Form):
    nama = forms.CharField(max_length=200)
    saldo = forms.IntegerField(initial=0) 
    kontak = forms.CharField(max_length=200)