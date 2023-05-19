from django.db import models

# Create your models here.
difficulty_choices = (
    ('easy', 'Easy'),
    ('medium', 'Medium'),
    ('intermediate', 'Intermediate'),
    ('hard', 'Hard')
)

rating_choices = (
    ('yum', 'Yum'),
    ('meh', 'Meh'),
    ('yuck', 'Yuck')
)

class Recipe(models.Model):
    name = models.CharField(max_length=50)
    cooking_time = models.FloatField()
    ingredients = models.CharField(max_length=255)
    difficulty = models.CharField(max_length=12, choices=difficulty_choices, default='na')
    rating = models.CharField(max_length=4, choices=rating_choices, default='na')

    def __str__(self):
        return str(self.name)