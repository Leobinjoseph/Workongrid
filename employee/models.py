from django.db import models

# Create your models here.

class Emp(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    birth_date = models.DateField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

