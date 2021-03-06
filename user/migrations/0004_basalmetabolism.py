# Generated by Django 4.0.4 on 2022-05-26 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_user_height_user_weight'),
    ]

    operations = [
        migrations.CreateModel(
            name='BasalMetabolism',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.IntegerField(help_text='How tall are you in cm?')),
                ('height', models.IntegerField(help_text='How much do you weight in kg?')),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female')], help_text='What is your gender?', max_length=255)),
                ('activity', models.CharField(choices=[('office job, no activities', 'office job, no activities'), ('office job, training twice per week', 'office job, training twice per week'), ('office job, training 3-4 times per week', 'office job, training 3-4 times per week'), ('office job, training 6 times per week', 'office job, training 6 times per week'), ('manual job, training 3-4 times per week', 'manual job, training 3-4 times per week'), ('manual job, training 6 times per week', 'manual job, training 6 times per week')], help_text='How active are you?', max_length=255)),
                ('target', models.CharField(choices=[('I would like lose weight', 'I would like lose weight'), ('I just want be as fit as I am', 'I just want be as fit as I am'), ('I want gain muscles/weight', 'I want gain muscles/weight')], help_text='What is your target?', max_length=255)),
            ],
        ),
    ]
