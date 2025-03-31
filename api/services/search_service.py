from ..models import StationLocation, LineOneRoute, LineThreeRoute, LineFiveRoute, LineSpecialRoute
import math
line1 = LineOneRoute.objects.all()
line3 = LineThreeRoute.objects.all()
line5 = LineFiveRoute.objects.all()
lineS = LineSpecialRoute.objects.all()
station = StationLocation.objects.all()

line_routes = {
            "1": LineOneRoute,
            "3": LineThreeRoute,
            "5": LineFiveRoute,
            "s": LineSpecialRoute
        }

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

def find_nearest_station(lat,lon):
    """ Find the nearest station of all station."""
    min_distance = float("inf")
    nearest_station = None
    for i in station:
        distance = (find_distance(i.latitude,i.longitude,lat,lon))
        if distance < min_distance:
            min_distance = distance
            nearest_station = i
    return nearest_station

def find_nearest_station_line(lat,lon,line):
    """Find the nearest station in specific line."""
    min_distance = float("inf")
    nearest_station = None
    for i in line:
        distance = (find_distance(i.station.latitude,i.station.longitude,lat,lon))
        if distance < min_distance:
            min_distance = distance
            nearest_station = i.station
    return nearest_station


def find_available_line(cur):
    """ Find Available line of current station"""
    available_lines = [
        line for line, model in line_routes.items() if model.objects.filter(station__id=cur).exists()
    ]
    return available_lines

def find_nearest_accessible_station(lat,lon,des):
    """ Find the nearest station that can reach destination station"""
    existed = find_available_line(des)
    nearest = {}
    min_distance = float('inf')
    nearest_line = ""
    for line in existed:
        stations = line_routes[line].objects.all()
        nearest_station = find_nearest_station_line(lat, lon, stations)
        nearest[line] = nearest_station
        distance = find_distance(lat, lon, nearest_station.latitude,nearest_station.longitude)
        if distance < min_distance:
                min_distance = distance
                nearest_line = line
    return nearest[nearest_line]


def available_station(cur):
    """ Find Available destination station that can reach by current station"""
    available_lines = find_available_line(cur)
    available_stations = set()
    for line in available_lines:
        if line == "1":
            stations = line1
        elif line == "3":
            stations = line3
        elif line == "5":
            stations = line5
        else:
            stations = lineS
        for station in stations:
            available_stations.add(station.station)
    # serializer = BusStopLocationSerializer(list(available_stations), many=True)
    return list(available_stations)

def find_bus_route(cur, des):
    """ Find Bus Route that user has to use """
    cur_line = set(find_available_line(cur))
    des_line = set(find_available_line(des))
    min_distance = float('inf')
    distance = 0
    shortest_line = ""
    available_line = cur_line.intersection(des_line)
    for line in available_line:
        cur_station_routes = line_routes[line].objects.filter(station__id=cur).order_by("order")
        des_station_routes = line_routes[line].objects.filter(station__id=des).order_by("order")

        if not cur_station_routes.exists() or not des_station_routes.exists():
            continue  # Skip this line if no valid stations exist

        cur_order = cur_station_routes.first().order  # Pick the first route
        des_order = des_station_routes.first().order
        if des_order >= cur_order:
            distance = des_order - cur_order
        else:
            all_station = line_routes[line].objects.count()
            distance = all_station - ((cur_order - des_order) + 1)

        if distance < min_distance:
            min_distance = distance
            shortest_line = line
    return shortest_line