# Generated by Django 4.0.4 on 2022-06-01 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0010_alter_recipe_carbs_alter_recipe_fats_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='carbs',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='food',
            name='fats',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='food',
            name='kcal',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='food',
            name='protein',
            field=models.FloatField(),
        ),
    ]