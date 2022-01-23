from turtle import title
from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length=256)
    abbrev = models.CharField(max_length=64)

    def __str__(self):
        return f"NAME: {self.name}, ABBREV: {self.abbrev}"

class Teacher(models.Model):
    name = models.CharField(max_length=256)
    surname = models.CharField(max_length=256)
    title = models.CharField(max_length=16, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering= ['created']
    
    def __str__(self):
        return f"{self.name} {self.surname}"

