# Generated by Django 5.1.6 on 2025-03-31 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_feedback_bus_stop'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='bus_stop',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
