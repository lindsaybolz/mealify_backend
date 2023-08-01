from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import AbstractUser
import datetime

from user_api.models import AppUser

# Create your models here.
# class User(AbstractUser):
#     """
#     Fields:
#     id | password | last_login | is_superuser | username | first_name | last_name | email | is_staff | is_active | date_joined | alergies | restrictions | prefrences 
#     """
#     def default_json():
#         return {}
#     alergies = models.JSONField(default=default_json)
#     restrictions = models.JSONField(default=default_json)
#     prefrences = models.JSONField(default=default_json)

#     def __str__(self):
#         return f'{self.first_name} {self.last_name}: {self.username}'

#     def to_dict(self):
#         return {
#             'id': self.id,
#             'last_login': self.last_login,
#             'is_superuser': self.is_superuser,
#             'username': self.username,
#             'first_name': self.first_name,
#             'last_name': self.last_name,
#             'email': self.email,
#             'is_staff': self.is_staff,
#             'is_active': self.is_active,
#             'date_joined': self.date_joined,
#             'alergies': self.alergies,
#             'restrictions': self.restrictions,
#             'prefrences': self.prefrences,
#         }


class Pantry(models.Model):
    user = models.OneToOneField(AppUser, on_delete=models.CASCADE)
    food_list = models.JSONField()
    updated = models.DateTimeField('Last Updated On', blank=True, null=True,default=datetime.date.today)    # staples = models.JSONField()
    
    def to_dict(self):
        return {
            'user': self.user,
            'food_list': self.food_list,
            'updated': self.updated,
        }


class Recipe(models.Model):
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    ingredients = models.JSONField()
    instructions = models.JSONField()
    nutritional_data = models.JSONField()
    url = models.URLField(max_length=200)
    user_state = models.IntegerField(validators=[MinValueValidator(-1), MaxValueValidator(1)])
