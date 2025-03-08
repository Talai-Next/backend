# Generated by Django 5.1.6 on 2025-02-13 11:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StationLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('station_code', models.CharField(max_length=10, verbose_name='Building Code')),
                ('name', models.CharField(max_length=255, verbose_name='Location Name')),
                ('latitude', models.FloatField(verbose_name='Latitude')),
                ('longitude', models.FloatField(verbose_name='Longitude')),
            ],
        ),
        migrations.CreateModel(
            name='LineOneRoute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField(unique=True)),
                ('station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.stationlocation')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='LineSpecialRoute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField(unique=True)),
                ('station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.stationlocation')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='LineThreeRoute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField(unique=True)),
                ('station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.stationlocation')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='LineFiveRoute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField(unique=True)),
                ('station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.stationlocation')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
    ]
