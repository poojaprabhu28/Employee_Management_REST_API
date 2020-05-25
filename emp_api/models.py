from django.db import models
#from django.contrib.auth.models import AbstractBaseUser
#from django.contrib.auth.models import PermissionsMixin

class Department(models.Model):
    """Department details"""
    




class Employee(models.Model):
    """Employee details"""
    name = models.CharField(max_length=255, blank=False)
    email = models.EmailField(max_length=255, unique=True)
    salary = models.IntegerField()
    contact_num = models.CharField(max_length=12, blank=False, unique=True)
    department = models.ForeignKey()
