from django.db import models

# Create your models here.
class Cat(models.Model):
    CAT_SIZES = [
        ("S", "Illegally smol"),
        ("M", "Medium"),
        ("C", "Chonk"),
    ]    
    name = models.CharField(max_length=30)
    size = models.CharField(max_length=1, choices=CAT_SIZES)
    upload = models.ImageField(upload_to ='media/')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
