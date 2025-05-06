from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

class Status(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

class Priority(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=7)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

class Reminder(models.Model):
    title = models.CharField(max_length = 100)
    description = RichTextField()
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    priority = models.ForeignKey(Priority, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title