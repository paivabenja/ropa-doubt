from django.db import models


# Create your models here.
class Prenda(models.Model):
    price = models.IntegerField()
    stock = models.IntegerField()
    type = models.CharField(max_length=200, blank=False)

    def __str__(self):
        return f'{self.type} de {self.price}. id: {self.id}'
