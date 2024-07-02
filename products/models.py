from django.db import models
class Product(models.Model):
    CATEGORY_CHOICES = [
        ('TRP','TRP'),
        ('C50','C50'),
        ('APOLLO','APOLLO'),
        ('G-STREET','G-STREET'),
        ('MINI-JET','MINI-JET'),
        ('CITY','CITY'),
        ('CRUZER','CRUZER'),
        ('ALPHA','ALPHA'),
        ('C100','C100'),
        ('110CC','110CC'),
        ('DJ50','DJ50'),
        ('FAME XR','FAME XR'),
        ('FIFTY','FIFTY'),
        ('C90','C90'),
        ('FAME GAMA','FAME GAMA'),
        ('FAME XS','FAME XS'),
        ('S50','S50'),
        ('MILANO','MILANO'),
        ('TANK','TANK'),
    ]
    
    name = models.CharField(max_length=100)
    reference = models.CharField(max_length=100, null=True, blank=True)
    position = models.CharField(max_length=50)
    active = models.BooleanField(default=True)
    category = models.CharField(max_length=20,choices=CATEGORY_CHOICES, null=True, blank=True)
    
    def __str__(self):
        return self.name