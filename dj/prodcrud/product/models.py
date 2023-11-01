from django.db import models

# Create your models here.
class Product(models.Model):
    pid = models.IntegerField() 
    pname =models.CharField(max_length=32)
    price =models.IntegerField()
    qty   =models.IntegerField() 

    class Meta:
        db_table="product"



