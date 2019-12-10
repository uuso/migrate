from django.db import models

# Create your models here.

class Dummy(models.Model):
    full_name = models.CharField(max_length=32, default="dummy")
    age = models.SmallIntegerField(default=25)
    def __str__(self):
        return "{}({})".format(self.full_name, self.age)