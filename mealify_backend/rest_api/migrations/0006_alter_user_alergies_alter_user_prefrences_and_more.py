# Generated by Django 4.2.3 on 2023-07-28 19:24

from django.db import migrations, models
import rest_api.models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0005_alter_user_prefrences'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='alergies',
            field=models.JSONField(default=rest_api.models.User.default_json),
        ),
        migrations.AlterField(
            model_name='user',
            name='prefrences',
            field=models.JSONField(default=rest_api.models.User.default_json),
        ),
        migrations.AlterField(
            model_name='user',
            name='restrictions',
            field=models.JSONField(default=rest_api.models.User.default_json),
        ),
    ]