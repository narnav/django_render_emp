from django.db import models

# Create your models here.
class Student(models.Model):
    sName = models.CharField(max_length=20)
    age = models.FloatField()

    def __str__(self):
        return self.sName
