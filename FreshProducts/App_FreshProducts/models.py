from django.db import models

# Create your models here.

class Licenze(models.Model):
    Code = models.IntegerField(primary_key=True)
    Data_sottoscrizione = models.DateTimeField('Data_sottoscrizione')
    Data_scadenza = models.DateTimeField('Data_scadenza')
    Prezzo = models.IntegerField()

class Punto_vendita(models.Model):
    Shop_code = models.AutoField(primary_key=True) # auto increment con id
    Nome = models.CharField(max_length=200)
    Indirizzo = models.CharField(max_length=200)
    Civico = models.CharField(max_length=200)
    Citta = models.CharField(max_length=200)
    Cap = models.IntegerField()
    Code = models.ForeignKey(Licenze, on_delete=models.CASCADE)

class Credenziali(models.Model):
    Username = models.CharField(primary_key=True, max_length=200)
    Password = models.CharField(max_length=200)
    Shop_code = models.ForeignKey(Punto_vendita, on_delete=models.CASCADE)

class Prodotto(models.Model):
    Barcode = models.IntegerField(primary_key=True)
    Nome = models.CharField(max_length=200)
    Marca = models.CharField(max_length=200)

class Magazzino(models.Model):
    class Meta:
        unique_together = (('Barcode', 'Shop_code'),)
    Barcode = models.ForeignKey(Prodotto, on_delete=models.CASCADE) # primary key
    Shop_code = models.ForeignKey(Punto_vendita, on_delete=models.CASCADE) # primary key
    Quantita = models.IntegerField()
    Reparto = models.CharField(max_length=200)
    Prezzo = models.FloatField()
    Scadenza = models.DateTimeField('Scadenza')

'''
models.AutoField()
models.IntegerField()
models.BooleanField()
'''