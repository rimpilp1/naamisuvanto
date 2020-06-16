from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone



class Saalis(models.Model):

    sukupuolet = [
        ('U','U'),
        ('N','N'),
        ('?','?')
    ]

    saaja = models.CharField(max_length = 300)
    paikka = models.CharField(max_length = 30)
    paino = models.CharField(max_length = 10)
    pituus = models.CharField(max_length = 10)
    viehe = models.CharField(max_length = 300)
    email = models.EmailField()
    saantipaiva = models.DateField(default=timezone.now(),blank=True)
    kuva = models.ImageField(upload_to="images/", default = "images/default.jpg")
    public = models.BooleanField()
    sukupuoli = models.CharField(max_length = 1,choices=sukupuolet,default='?')

    #authenticator
    #poster
    #phonenumber
    def __str__(self): 
        return "Saaja: " + self.saaja+ " Paikka: " + self.paikka + " Viehe: " + self.viehe + " Paino:" + self.paino + " Pituus: " + self.pituus + " Paiva: "
        
    class Meta:
        permissions = (
        ("publish","Allows publishing of saalistilasto objects"),
        )
# Create your models here.
