from django.db import models

# Create your models here.
class ORGANIZATION(models.Model):
    NAME_ORG = models.CharField(max_length=30)
    FIO_LEAD = models.CharField(max_length=45)
    PH_NUM = models.CharField(max_length=15)
    ADDRESS = models.CharField(max_length=45)
    ORGANIZATION_ID = models.IntegerField()


class EMPLOYEES(models.Model):
    EMPLOYEE_ID = models.IntegerField()
    JOB_TITLE_ID = models.IntegerField()
    FIO_EMPL = models.CharField(max_length=45)


class JOB_TITLE(models.Model):
    JOB_TITLE_ID = models.IntegerField()
    SALARY = models.IntegerField()
    NAME = models.CharField(max_length=45)
    DUTY = models.CharField(max_length=45)


class CLIENTS(models.Model):
    CLIENT_ID = models.IntegerField()
    FIO_CLIENT = models.CharField(max_length=45)


class AUTOMOBILE(models.Model):
    MODEL = models.CharField(max_length=45)
    AUTOMOBILE_ID = models.IntegerField()
    GENERATION = models.CharField(max_length=45)
    GEAR_BOX = models.CharField(max_length=45)
    DRIVE = models.CharField(max_length=45)
    ENGINE = models.CharField(max_length=45)
    BODY = models.CharField(max_length=45)
    WHEEL = models.CharField(max_length=45)
    ENGINE_POWER = models.IntegerField()
    CAPACITY = models.FloatField()
    def __str__(self):
        return self.MODEL

class ADD_EQUIP(models.Model):
    ID_AE = models.IntegerField()
    NAME_AE = models.CharField(max_length=45)


class ADD_SERV(models.Model):
    ID_AS = models.IntegerField()
    NAME_AS = models.CharField(max_length=45)


class CHECK(models.Model):
    ID_AE = models.IntegerField()
    ID_AS = models.IntegerField()
    AUTOMOBILE_ID = models.IntegerField()
    FIN_COST = models.IntegerField()
    ID_COST = models.IntegerField()


class AGREEMENT(models.Model):
    AGREEMENT_ID = models.IntegerField()
    EMPLOYEE_ID = models.IntegerField()
    CLIENT_ID = models.IntegerField()
    DATE = models.DateTimeField()
    ID_COST = models.IntegerField()
    ORGANIZATION_ID = models.IntegerField()