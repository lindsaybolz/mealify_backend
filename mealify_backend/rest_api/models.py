from django.db import models
# from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

# Create your models here.
class User(User):
    alergies = models.JSONField()
    restrictions = models.JSONField()
    prefrences = models.JSONField()
    


class Pantry(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    food_list = models.JSONField()
    updated = models.DateTimeField('Last Updated On')
    staples = models.JSONField()


class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    ingredients = models.JSONField()
    instructions = models.JSONField()
    nutritional_data = models.JSONField()
    url = models.URLField(max_length=200)
    user_state = models.IntegerField(validators=[MinValueValidator(-1), MaxValueValidator(1)])
