from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Pantry(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    food_list = models.JSONField()
    updated = models.DataTimeField('Last Updated On')
    staples = models.JSONField()

class Recipe(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    ingredients = models.JSONField()
    instructions = models.JSONField()
    nutritional_data = models.JSONField()
    url = models.URLField(max_length=200)
    user_state = models.IntegerField(validators=[MinValueValidator(-1), MaxValueValidator(1)])
