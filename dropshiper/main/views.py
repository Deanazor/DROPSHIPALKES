from django.shortcuts import render
from django.http import HttpResponse
from .models import Konsumen
from .forms import KonsumenForm

# Create your views here.
def homepage(request):
    return render(request=request,
                  template_name='main/home.html',
                  context={"konsumen": Konsumen.objects.all})

def register(request):
    if request.method == 'POST':
        form = KonsumenForm(request.POST)
        if form.is_valid():
            new_nama = form.cleaned_data['nama']
            new_saldo = form.cleaned_data['saldo']
            new_kontak = form.cleaned_data['kontak']
            new_konsumen = Konsumen(nama=new_nama, saldo=new_saldo, kontak=new_kontak)
            new_konsumen.save()
            return HttpResponse("Register Berhasil")
    else:
        form = KonsumenForm()

    return render(request=request, template_name='main/register.html', context={'form':form})
