from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Inpile(models.Model):
    task = models.CharField(max_length=100)
    task_description = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.task
