from django.db import models

# Create your models here.

class Dummy(models.Model):
    full_name = models.CharField(max_length=32, default="dummy")
    def __str__(self):
        return self.full_name