from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=24)
    surname = models.CharField(max_length=25)
    bio = models.TextField()
    salary = models.IntegerField(default=0)
    start_work_time = models.TimeField()
    end_work_time = models.TimeField()
