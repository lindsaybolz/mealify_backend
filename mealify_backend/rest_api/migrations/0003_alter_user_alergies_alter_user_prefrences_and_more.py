# Generated by Django 4.2.3 on 2023-07-28 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0002_alter_recipe_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='alergies',
            field=models.JSONField(default='{}'),
        ),
        migrations.AlterField(
            model_name='user',
            name='prefrences',
            field=models.JSONField(default='{}'),
        ),
        migrations.AlterField(
            model_name='user',
            name='restrictions',
            field=models.JSONField(default='{}'),
        ),
    ]