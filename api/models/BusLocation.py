from django.db import models

class BusLocation(models.Model):
    station_code = models.CharField(max_length=10, verbose_name="Building Code")
    name = models.CharField(max_length=255, verbose_name="Location Name")
    latitude = models.FloatField(verbose_name="Latitude")
    longitude = models.FloatField(verbose_name="Longitude")

    def __str__(self):
        return f"{self.station_code} - {self.name}"
