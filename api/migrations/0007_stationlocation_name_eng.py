# Generated by Django 5.1.7 on 2025-04-01 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_feedback_bus_stop'),
    ]

    operations = [
        migrations.AddField(
            model_name='stationlocation',
            name='name_eng',
            field=models.CharField(default='', max_length=255, verbose_name='Location Name English'),
        ),
    ]
