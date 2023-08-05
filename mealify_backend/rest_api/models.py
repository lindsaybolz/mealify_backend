from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import AbstractUser
import datetime

from user_api.models import AppUser


class Pantry(models.Model):
    user = models.OneToOneField(AppUser, on_delete=models.CASCADE)
    food_list = models.JSONField()
    updated = models.DateTimeField('Last Updated On', blank=True, null=True,default=datetime.date.today)    # staples = models.JSONField()
    
    def to_dict(self):
        return {
            'id': self.pk,
            'user': self.user.pk,
            'food_list': self.food_list,
            'updated': self.updated,
        }


class Recipe(models.Model):
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    ingredients = models.JSONField()
    instructions = models.JSONField()
    nutritional_data = models.DecimalField(decimal_places=15, max_digits=17)
    url = models.URLField(max_length=200)
    user_state = models.IntegerField(validators=[MinValueValidator(-1), MaxValueValidator(1)])

    def to_dict(self):
        return {
            'id': self.pk,
            'user': self.user.pk,
            'name': self.name,
            'ingredients': self.ingredients,
            'instructions': self.instructions,
            'nutritional_data': self.nutritional_data,
            'url': self.url,
            'user_state': self.user_state,
        }
