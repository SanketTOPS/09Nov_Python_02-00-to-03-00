from django.db import models

# Create your models here.
class Studinfo(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    dob=models.DateField()
    city=models.CharField(max_length=20)

