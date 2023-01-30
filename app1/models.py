from django.db import models

# Create your models here.
class Signup(models.Model):
    Name=models.CharField(max_length=20)
    Age=models.IntegerField()
    Email=models.EmailField()
    Password=models.CharField(max_length=9)


class Image(models.Model):
    Photo=models.ImageField(upload_to='media/',null=True,blank=True)

class Signup1(models.Model):
    Name=models.CharField(max_length=20)
    Age=models.IntegerField()
    Photo=models.ImageField(upload_to='media/',null=True,blank=True)
    Email=models.EmailField()
    Password=models.CharField(max_length=9)
    

class Image1(models.Model):
    Name=models.CharField(max_length=20)
    Brand=models.CharField(max_length=20)
    Model=models.CharField(max_length=20)
    year=models.CharField(max_length=20)
    Photo=models.ImageField(upload_to='media/',null=True,blank=True)
