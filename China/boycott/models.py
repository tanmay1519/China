from django.db import models

# Create your models here.
class Product (models.Model):
    PrId = models.AutoField(primary_key=True)
    ChinaPr = models.CharField(max_length=100,default='')
    category = models.CharField(max_length=100,default='')
    IndPr1 = models.CharField(max_length=100,default='')
    IndPr2 = models.CharField(max_length=100,default='')
    WorPr1 = models.CharField(max_length=100,default='')
    WorPr2 = models.CharField(max_length=100,default='')
