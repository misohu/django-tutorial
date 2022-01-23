from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length=256)
    abbrev = models.CharField(max_length=64)

    def __str__(self):
        return f"NAME: {self.name}, ABBREV: {self.abbrev}"
