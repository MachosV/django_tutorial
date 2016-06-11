from __future__ import unicode_literals
from django.core.validators import MinValueValidator
from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=30)
    is_manager = models.BooleanField()

    def __str__(self):
        return self.name+" "+self.surname


class Note(models.Model):
    poster = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=100)
    color = models.CharField(max_length=6)

    def __str__(self):
        return self.text+" "+self.poster.surname


class Storage(models.Model):
    site = models.CharField(max_length=15)
    location = models.CharField(max_length=5)

    def __str__(self):
        return self.site+" "+self.location

    class Meta:
        unique_together = ('site', 'location',)


class Part(models.Model):
    code = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=50)
    price = models.FloatField(validators=[MinValueValidator(0)])
    quantity = models.IntegerField(validators=[MinValueValidator(0)])
    storage = models.ManyToManyField(Storage)

    def get_absolute_url(self):
        return reverse('work_as:newPart')

    def __str__(self):
        return self.code+" "+self.description

