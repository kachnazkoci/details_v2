# Generated by Django 4.0.4 on 2022-05-28 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_user_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.IntegerField(default=25),
            preserve_default=False,
        ),
    ]
