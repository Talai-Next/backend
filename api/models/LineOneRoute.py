from django.db import models
from .BusLocation import BusLocation

class LineOneRoute(models.Model):
    order = models.PositiveIntegerField(unique=True)
    station = models.ForeignKey(BusLocation, on_delete=models.CASCADE)

    class Meta:
        ordering = ["order"]

    def save(self, *args, **kwargs):
        if not self.order:
            last_order = LineOneRoute.objects.aggregate(models.Max("order"))['order__max']
            self.order = (last_order or 0) + 1
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.station_code} - {self.name}"


