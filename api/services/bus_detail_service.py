from . import fetch_bus_data
from ..models import StationLocation, LineOneRoute, LineThreeRoute, LineFiveRoute, LineSpecialRoute
from .search_service import find_nearest_station_line
from geopy.distance import distance as geopy_distance
import time
import threading
from itertools import chain

FETCH_INTERVAL = 1
BUS_NEXT_STATION = {}
BUS_ARRIVAL_TIME = {}
bus_arrival_time = {
    "1": [],
    "3": [],
    "5": [],
    "SP": []
}
station = StationLocation.objects.all()

line_routes = {
    "1": LineOneRoute,
    "3": LineThreeRoute,
    "5": LineFiveRoute,
    "SP": LineSpecialRoute
}


def find_current_station(lat, lon, line, order):
    """
    Check if the bus has entered the 50m radius of the next station and update the order.
    """
    is_next_station = line_routes[line].objects.filter(order=order + 1)

    # if last station
    if not is_next_station:
        # update order to first station
        return 1
    next_station = line_routes[line].objects.get(order=order + 1).station

    distance = geopy_distance((lat, lon), (next_station.latitude, next_station.longitude)).meters
    if distance <= 50:
        order = order + 1
    return order


def predict_arrival_time(lat, lon, line, speed, order):
    """Estimate arrival time from speed and distance between each station in a circular route."""
    stations = line_routes[line].objects.all().order_by("order")
    n = line_routes[line].objects.count()
    arrival_time = []

    # check next station
    next_order = (order % n) + 1
    next_station = line_routes[line].objects.filter(order=next_order).first()

    total_distance = geopy_distance((lat, lon), (next_station.station.latitude, next_station.station.longitude)).meters

    for i in range(1, n):
        current_order = (order + i - 1) % n + 1
        next_order = (current_order % n) + 1

        current_station = line_routes[line].objects.get(order=current_order)
        next_station = line_routes[line].objects.filter(order=next_order).first()

        if next_station:
            total_distance += geopy_distance(
                (current_station.station.latitude, current_station.station.longitude),
                (next_station.station.latitude, next_station.station.longitude)
            ).meters

        time_estimate = f"{(total_distance / speed) / 60:.1f}"
        arrival_time.append({
            "station_id": current_station.station.id,
            "time": time_estimate
        })

    bus_arrival_time[line].append(arrival_time)
    return arrival_time


def overall_arrival_time(line):
    station_dict = {}
    for entry in chain(*bus_arrival_time[line]):
        station_id = entry["station_id"]
        time = float(entry["time"])  # Convert time to int for comparison

        if station_id not in station_dict or time < station_dict[station_id]["time"]:
            station_dict[station_id] = {"station_id": station_id, "time": time}

    return list(station_dict.values())


def update_bus_locations():
    """ update bus current station every 1 second """
    global BUS_NEXT_STATION
    global BUS_ARRIVAL_TIME

    while True:
        buses = fetch_bus_data()

        for bus in buses:
            obj_id = bus.get("id")
            bus_id = bus.get("bus_id")
            lat = bus.get("latitude")
            lon = bus.get("longitude")
            line = str(bus.get("line"))
            speed = bus.get("speed")

            if obj_id is None or lat is None or lon is None or line not in line_routes:
                continue

            # Initialize start station
            if obj_id not in BUS_NEXT_STATION:
                start_station = find_nearest_station_line(lat, lon, line_routes[line].objects.all())
                cur_order = line_routes[line].objects.filter(station=start_station).order_by('order').first().order
                current_station = start_station.id
                BUS_NEXT_STATION[obj_id] = {
                    "id": obj_id,
                    "bus_id": bus_id,
                    "station_id": current_station,
                    "order": cur_order,
                    "line": line,
                }
            else:
                cur_order = BUS_NEXT_STATION[obj_id]["order"]

            # Find current station
            order = find_current_station(lat, lon, line, cur_order)
            current_station = line_routes[line].objects.get(order=order).station.id
            BUS_NEXT_STATION[obj_id] = {
                "bus_id": bus_id,
                "station_id": current_station,
                "order": order,
                "line": line,
            }

            t = predict_arrival_time(lat, lon, line, speed, order)
            BUS_ARRIVAL_TIME[obj_id] = {
                "line": line,
                "time": overall_arrival_time(line)
            }

        time.sleep(FETCH_INTERVAL)


def start_update_bus_locations():
    thread = threading.Thread(target=update_bus_locations, daemon=True)
    thread.start()
