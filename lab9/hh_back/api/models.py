from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    city = models.CharField(max_length=255)
    address = models.TextField(blank=True)

class Vacancy(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    salary = models.FloatField()
    company = models.ForeignKey('Company', on_delete= models.PROTECT, null=True)