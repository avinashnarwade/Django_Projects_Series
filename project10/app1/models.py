from django.db import models

# Create your models here.

class UserRegister(models.Model):
    name = models.CharField(max_length=20)
    uname = models.CharField(max_length=15,primary_key=True)
    password= models.CharField(max_length = 15)

class Person(models.Model):
    name=models.CharField(max_length=30)
    age=models.IntegerField()
class Course(models.Model):
    cname=models.CharField(max_length=20)
    fee=models.FloatField()