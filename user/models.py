from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=200, blank=False)
    mail = models.CharField(max_length=200, blank=False)
    password = models.CharField(max_length=200, blank=False)

    def __str__(self):
        return self.username
