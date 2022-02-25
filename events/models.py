from tabnanny import verbose
from django.db import models

# Create your models here.

class Event(models.Model):
    id = models.AutoField(primary_key=True)
    class JenisKelamin(models.TextChoices):
        LAKI_LAKI = 'L'
        PEREMPUAN = 'P'
    jenis_kelamin = models.CharField(
        max_length=1,
        choices=JenisKelamin.choices,
        default=JenisKelamin.LAKI_LAKI,
    )
    nama = models.CharField(max_length=50)
    alamat = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=6)
    other = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'events'

    def __str__(self):
        return self.nama
