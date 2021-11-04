from django.db import models
from django.urls import reverse

# Create your models here.

EXERCISES = (
    ('M', 'Morning'),
    ('A', 'Afternoon'),
    ('E', 'Evening')
)


class Pokemon(models.Model):
    name = models.CharField(max_length=100)
    level = models.IntegerField(default=0)
    element = models.CharField(max_length=100)
    description = models.TextField(max_length=250)

    def __str__(self):
        return f'{self.name} is a {self.element} type Pokemon.'

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pokemon_id': self.id})


class Training(models.Model):
    date = models.DateField('Training Date')
    exercise = models.CharField(
        'Meal Period',
        max_length=1,
        choices=EXERCISES,
        default=EXERCISES[0][0]
    )

    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.get_exercise_display()} on {self.date}.'
