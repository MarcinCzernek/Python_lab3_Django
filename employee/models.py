from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    salary = models.IntegerField()


