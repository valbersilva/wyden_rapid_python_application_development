from django.db import models

# Create your models here.
class Car(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    marca = models.CharField(max_length=100)
    ano = models.IntegerField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    cor = models.CharField(max_length=100)
    image = models.ImageField(upload_to='fotos/%Y/%m/%d/', blank=True)

    def __str__(self):
        return self.marca + ' ' + self.name