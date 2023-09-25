from django.db import models

# Create your models here.

class destination(models.Model):
   Firstname = models.CharField(max_length=20)
   Lastname = models.CharField(max_length=10)
   Marks = models.IntegerField()
   Department = models.CharField(max_length=10)
