# Generated by Django 4.0.3 on 2022-05-21 19:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0003_blog'),
    ]

    operations = [
        migrations.CreateModel(
            name='Amount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='recipe',
            name='weight',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blog',
            name='description',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='ingredients',
        ),
        migrations.AddField(
            model_name='recipe',
            name='ingredients',
            field=models.ManyToManyField(through='food.Amount', to='food.food'),
        ),
        migrations.AddField(
            model_name='amount',
            name='food_choice_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food.recipe'),
        ),
        migrations.AddField(
            model_name='amount',
            name='recipe_weight_food',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food.food'),
        ),
    ]
