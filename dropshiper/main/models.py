from django.db import models

# Create your models here.
class Konsumen(models.Model):
    nama = models.CharField(max_length=200)
    saldo = models.IntegerField()
    kontak = models.CharField(max_length=200)

    def __str__(self):
        return self.nama