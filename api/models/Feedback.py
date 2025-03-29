from django.db import models


class Feedback(models.Model):
    bus_station = models.ForeignKey(
        "StationLocation", on_delete=models.CASCADE, verbose_name="Bus Station"
    )
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

    def __str__(self):
        return f"{self.name}"
