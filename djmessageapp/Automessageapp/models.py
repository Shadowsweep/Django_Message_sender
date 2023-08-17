from django.db import models

# Create your models here.
class Customers(models.Model):
    # policyno = models.CharField(max_length=70,blank=False,default='',primary_key=True)
    policyno = models.CharField(max_length=150, blank=False,default='')
    customername = models.CharField(max_length=70, blank=False,default='')
    lastdate = models.CharField(max_length=150, blank=False,default='')
    hourtime = models.CharField(max_length=150, blank=False,default='')
    mintime = models.CharField(max_length=150, blank=False,default='')
    contactno = models.CharField(max_length=150, blank=False,default='')