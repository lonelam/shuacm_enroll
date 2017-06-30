from django.db import models
from django.utils import timezone
# Create your models here.


class Acmer(models.Model):

    name = models.CharField(max_length = 20)
    stuno = models.CharField(max_length=20)
    major = models.CharField(max_length = 20)
    phone = models.CharField(max_length = 12)
    email = models.EmailField()

    def __str__(self):
        return self.name + ',' + str(self.stuno)


class Lecture(models.Model):
    topic = models.CharField(max_length = 200)
    leader = models.ForeignKey(Acmer, related_name = 'PublishedLec')
    members = models.ManyToManyField(Acmer, related_name = 'PaticipatedLec')
    starttime = models.DateTimeField()
