from django.db import models
# from .models import Student
# Create your models here.
"""
model: python class used to represent a database table

syntax:
class Model_name(models.Model):
    feild.......

"""
class Student(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    age=models.IntegerField(default=18)
    marks=models.IntegerField()
    city=models.CharField(max_length=50)
    email=models.CharField(max_length=100,unique=True)
    is_active=models.BooleanField(default=True)

    def __str__(self):
        return self.name
    

