from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Users(models.Model):
    name=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    DOB=models.DateField()
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    place=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    pin=models.CharField(max_length=100)
    district=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    status=models.CharField(max_length=100)
    AUTHUSER=models.OneToOneField(User,on_delete=models.CASCADE)


class Police(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    photo=models.CharField(max_length=200)
    phoneno=models.CharField(max_length=100)
    post=models.CharField(max_length=100)
    place=models.CharField(max_length=100)
    pin=models.CharField(max_length=100)
    USER=models.OneToOneField(User,on_delete=models.CASCADE)

class Authority(models.Model):
    authorityname=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    photo=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    place=models.CharField(max_length=100)
    pin=models.CharField(max_length=100)
    district=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    AUTHUSER=models.OneToOneField(User,on_delete=models.CASCADE)

class Criminals(models.Model):
    criminalname=models.CharField(max_length=100)
    photo=models.CharField(max_length=100)
    identification=models.CharField(max_length=100)
    dob=models.CharField(max_length=100)
    offense=models.CharField(max_length=100)
    height=models.CharField(max_length=100)
    weight=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    phoneno=models.CharField(max_length=100)

class Complaint(models.Model):
    date=models.DateField()
    complaint=models.CharField(max_length=100)
    reply=models.CharField(max_length=100)
    status=models.CharField(max_length=100)
    AUTHUSER=models.ForeignKey(User,on_delete=models.CASCADE)

class Criminaldetection(models.Model):
    date=models.DateField()
    photo=models.CharField(max_length=100)
    time=models.CharField(max_length=100)
    CRIMINAL=models.ForeignKey(Criminals,on_delete=models.CASCADE)

class Objectdetection(models.Model):
    log=models.CharField(max_length=100)
    place=models.CharField(max_length=100)
    time=models.CharField(max_length=100)
    date=models.DateField()


class logs(models.Model):
    date = models.DateField()
    time = models.TimeField()
    result = models.CharField(max_length=100)
    USER = models.ForeignKey(Users,on_delete=models.CASCADE)


