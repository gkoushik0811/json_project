from django.db import models
from django.utils import timezone
# Create your models here.
class Employee(models.Model):
    eno=models.IntegerField()
    ename=models.CharField(max_length=55)
    eLocation=models.CharField(max_length=55)
    start_time=models.DateTimeField()
    end_time=models.DateTimeField()
