from django.db import models
from django.utils import timezone
# Create your models here.

class Acmer(models.Model):
    name = models.CharField(max_length = 20)
    stuno = models.IntegerField()
    phone = models.CharField(max_length = 12)
    email = models.EmailField()
    def __str__(self):
        return self.name + ',' + str(self.stuno)
