# Generated by Django 5.1.6 on 2025-03-28 13:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_obstacletype_obstacleposition'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('passenger_density', models.IntegerField(choices=[(1, 'Very Low'), (2, 'Low'), (3, 'Medium'), (4, 'High'), (5, 'Very High')], verbose_name='Passenger Density')),
                ('comment', models.CharField(max_length=255, verbose_name='Obstacle Type')),
                ('bus_station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.stationlocation', verbose_name='Bus Station')),
            ],
        ),
    ]
