from ..models import StationLocation, LineOneRoute, LineThreeRoute, LineFiveRoute, LineSpecialRoute
import math
line1 = LineOneRoute.objects.all()
line3 = LineThreeRoute.objects.all()
line5 = LineFiveRoute.objects.all()
lineS = LineSpecialRoute.objects.all()
station = StationLocation.objects.all()


def find_distance(lat1, lon1, lat2, lon2):
    """ Find distance between 2 place on earth in meter."""
    # Convert decimal degrees to radians
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    r = 6371
    # Return distance in meters
    return r * c * 1000