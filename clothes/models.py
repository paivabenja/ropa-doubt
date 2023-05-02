from django.db import models
from clothes.choices import sizes


# Create your models here.
class Clothes(models.Model):
    price = models.IntegerField()
    type = models.CharField(max_length=200)
    sizes = models.CharField(max_length=3, choices=sizes, default="l")

    def __str__(self):
        return f"{self.type} de {self.price}, número {self.id}"
