from django.db import models

# Create your models here.
class ORGANIZATION(models.Model):
    NAME_ORG = models.CharField(max_length=30)
    FIO_LEAD = models.CharField(max_length=45)
    PH_NUM = models.CharField(max_length=15)
    ADDRESS = models.CharField(max_length=45)
    ORGANIZATION_ID = models.IntegerField()