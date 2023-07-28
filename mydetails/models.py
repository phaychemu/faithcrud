from django.db import models

# Create your models here.
class Student(models.Model):
    Name=models.CharField(max_length=200)
    course=models.CharField(max_length=200)
    admission=models.IntegerField()

    class Meta:
        db_table="student"

