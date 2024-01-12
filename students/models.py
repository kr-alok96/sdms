from django.db import models

# Create your models here.
class Student(models.Model):
    student_admnNo = models.IntegerField()
    student_name = models.CharField(max_length = 50)
    student_dob = models.DateField()

    
