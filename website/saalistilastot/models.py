from django.conf import settings
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone



class Saalis(models.Model):

    sukupuolet = [
        ('U','U'),
        ('N','N'),
        ('-','-')
    ]

    lajit = [
        ('Taimen','Taimen'),
        ('Lohi','Lohi'),
    ]

    saaja = models.CharField(max_length = 50)
    paikka = models.CharField(max_length = 10)
    laji = models.CharField(max_length = 10, choices = lajit, default = 'Lohi')
    vapautettu = models.BooleanField(default = False)
    paino = models.DecimalField(max_digits = 10, decimal_places=2, null =True)
    pituus = models.DecimalField(max_digits = 10, decimal_places=0, null=True, blank=True)
    viehe = models.CharField(max_length = 20, default = '-')
    email = models.EmailField(null = True)
    saantipaiva = models.DateField(default=timezone.now)
    kuva = models.ImageField(upload_to="images/", default = "images/default.jpg")
    public = models.BooleanField(default=False)
    sukupuoli = models.CharField(max_length = 1,choices=sukupuolet,default='-')

    #authenticator
    #poster
    #phonenumber
    def __str__(self): 
        if self.public:
            return str(self.saantipaiva) + " | " + self.saaja + " | " + str(self.paino)
        else:
            return "X " + str(self.saantipaiva) + " | " + self.saaja + " | " + str(self.paino)
        
    class Meta:
        permissions = (
        ("publish","Allows publishing of saalistilasto objects"),
        )
# Create your models here.
