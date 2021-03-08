from django.db import models

# Create your models here.
class products(models.Model):
    name=models.CharField(max_length=30)
    price=models.IntegerField()
    catageory=models.CharField(max_length=10)
    subcatageory=models.CharField(max_length=10)
    photo = models.ImageField(upload_to='static/img')
    quentity=models.IntegerField()
    description=models.CharField(max_length=200)
    brand=models.CharField(max_length=10)
    longDescription=models.CharField(max_length=1000)


def __str__(self):
    return self.title

