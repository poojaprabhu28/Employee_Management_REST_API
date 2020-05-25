from django.db import models
#from django.contrib.auth.models import AbstractBaseUser
#from django.contrib.auth.models import PermissionsMixin

class Department(models.Model):
    """Department details"""
    dept_id = models.CharField(max_length=3, unique=True)
    dept_name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.dept_id
        return self.dept_name

class Employee(models.Model):
    """Employee details"""
    emp_id = models.CharField(max_length=5, unique=True, blank=False)
    emp_name = models.CharField(max_length=255, blank=False)
    email = models.EmailField(max_length=255, unique=True)
    salary = models.IntegerField()
    contact_num = models.CharField(max_length=12, blank=False, unique=True)
    department = models.ForeignKey(Department, related_name='department', on_delete=models.CASCADE)
    join_date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.emp_id
        return self.emp_name
