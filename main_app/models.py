from django.db import models

# Create your models here.

class Pokemon(models.Model):
    name = models.CharField(max_length=100)
    level = models.IntegerField(default=0)
    element = models.CharField(max_length=100)
    description = models.TextField(max_length=250)

    def __str__(self):
        return f'{self.name} is a {self.element} type Pokemon.'