from django.db import models

# Create your models here.


class ToDolist(models.Model):
    task_start_time = models.DateTimeField(null=True, blank=True)
    content = models.TextField(max_length=256)
    status = models.TextField(max_length=50)
    category = models.TextField(max_length=50)
    priority = models.BigIntegerField()


class MangedDay(models.Model):
    task_start_time = models.TextField(max_length=100) #models.DateTimeField()
    content = models.TextField(max_length=256,null=True, blank=True)
    status = models.TextField(max_length=50,null=True, blank=True)
    category = models.TextField(max_length=50,null=True, blank=True)
    priority = models.BigIntegerField(null=True, blank=True)
