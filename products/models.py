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
        
    ]
    
    name = models.CharField(max_length=100)
    reference = models.CharField(max_length=100)
    position = models.CharField(max_length=50)
    active = models.BooleanField(default=True)
    category = models.CharField(max_length=20,choices=CATEGORY_CHOICES, default='TRP')
    
    def __str__(self):
        return self.name
