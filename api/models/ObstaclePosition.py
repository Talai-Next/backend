from django.db import models
from .Obstacle import ObstacleType


class ObstaclePosition(models.Model):
    latitude = models.FloatField(verbose_name="Latitude")
    longitude = models.FloatField(verbose_name="Longitude")
    obstacle_type = models.ForeignKey(ObstacleType, on_delete=models.CASCADE, verbose_name="Obstacle Type")

    def __str__(self):
        return f"{self.obstacle_type} at {self.latitude}, {self.longitude}"
