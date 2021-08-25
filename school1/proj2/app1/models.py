from django.db import models

# Create your models here.
class Attendence(models.Model):
    Name = models.CharField(max_length=20)
    datefield =models.CharField(max_length=50)
    status = models.CharField(max_length=20)

class Numofstudents(models.Model):
    Name=models.CharField(max_length=20)
    Rollno=models.IntegerField()
    Fathername=models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    address=models.CharField(max_length=20)

