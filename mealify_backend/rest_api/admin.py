from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Pantry, Recipe

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Pantry)
admin.site.register(Recipe)
