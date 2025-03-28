from django.db import models


class ObstacleType(models.Model):
    name = models.CharField(max_length=255, verbose_name="Obstacle Type")

    def __str__(self):
        return f"{self.name}"
