from django.db import models


class Feedback(models.Model):
    bus_id = models.IntegerField()
    bus_line = models.CharField()
    passenger_density = models.IntegerField(
        verbose_name="Passenger Density",
        choices=[
            (1, "Very Low"),
            (2, "Low"),
            (3, "Medium"),
            (4, "High"),
            (5, "Very High"),
        ],
    )
    comment = models.CharField(max_length=255, verbose_name="Obstacle Type")
