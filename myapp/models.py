from django.db import models

# Create your models here.
class products(models.Model):
    name=models.CharField(max_length=30)
    price=models.IntegerField()
    catageory=models.CharField(max_length=10)
    subcatageory=models.CharField(max_length=10)
    photo = models.ImageField(upload_to='static/img')
    quentity=models.IntegerField()
    description=models.CharField(max_length=100)
    brand=models.CharField(max_length=10)

class Items(models.Model):
    name=models.CharField(max_length=30)
    price=models.IntegerField()
    catageory=models.CharField(max_length=10)
    subcatageory=models.CharField(max_length=10)
    photo = models.ImageField(upload_to='static/img')
    quentity=models.IntegerField()
    description=models.CharField(max_length=100)
    brand=models.CharField(max_length=10)
