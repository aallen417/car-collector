# Generated by Django 4.2.16 on 2024-09-26 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_car_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='type',
            field=models.CharField(choices=[('S', 'Sport'), ('L', 'Sedan'), ('C', 'Crossover/SUV'), ('T', 'Truck')], default='S', max_length=1),
        ),
    ]
