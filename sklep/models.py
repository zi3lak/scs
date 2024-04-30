from django.db import models

class Produkt(models.Model):
    nazwa = models.CharField(max_length=200)
    opis = models.TextField()
    cena = models.DecimalField(max_digits=8, decimal_places=2)
    dostepnosc = models.BooleanField(default=True)

    def __str__(self):
        return self.nazwa

