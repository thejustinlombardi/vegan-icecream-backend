from django.db import models

# Create your models here.


class IceCream(models.Model):
    '''set up IceCream class'''
    brand = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    alternatives = models.CharField(max_length=100)
    site = models.TextField()
    photo_url = models.TextField()

    def __str__(self):
        '''dunder method'''
        return self.brand
