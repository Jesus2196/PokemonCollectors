from django.db import models
from django.urls import reverse
from datetime import date

# Create your models here.

EXERCISES = (
    ('M', 'Morning'),
    ('A', 'Afternoon'),
    ('E', 'Evening')
)


class Item(models.Model):
    name = models.CharField(max_length=50)
    effect = models.TextField(max_length=150)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('items_detail', kwargs={'pk': self.id})


class Pokemon(models.Model):
    name = models.CharField(max_length=100)
    level = models.IntegerField(default=0)
    element = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    items = models.ManyToManyField(Item)

    def __str__(self):
        return f'{self.name} is a {self.element} type Pokemon.'

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pokemon_id': self.id})

    def trained_for_today(self):
        return self.training_set.filter(date=date.today()).count() >= len(EXERCISES)


class Training(models.Model):
    date = models.DateField('Training Date')
    exercise = models.CharField(
        'Exercise Time:',
        max_length=1,
        choices=EXERCISES,
        default=EXERCISES[0][0]
    )

    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.get_exercise_display()} on {self.date}.'

    class Meta:
        ordering = ['-date']