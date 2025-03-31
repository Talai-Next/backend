from ..models import StationLocation, LineOneRoute, LineThreeRoute, LineFiveRoute, LineSpecialRoute
import requests
from .search_service import find_nearest_station_line, find_distance
import time
import threading
from itertools import chain

FETCH_INTERVAL = 1
BUS_LOCATIONS = {}
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

def fetch_bus_data():
    """Fetch data from external API."""
    url = "http://127.0.0.1:8080/api/buses"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching bus data: {e}")
        return []

def find_current_station(lat, lon, line, order):
    """
    Check if the bus has entered the 300m radius of the next station and update the order.
    """
    is_next_station = line_routes[line].objects.filter(order=order+1)

    # if last station
    if not is_next_station:
        # update order to first station
        return 1
    next_station = line_routes[line].objects.get(order=order+1).station

    distance = find_distance(lat,lon,next_station.latitude,next_station.longitude)
    if distance <= 300:
        order = order + 1
    return order

def predict_arrival_time(lat, lon, line, speed):
    stations = line_routes[line].objects.all().order_by("order")
    arrival_time = []
    for i in stations:
        distance = find_distance(lat,lon,i.station.latitude,i.station.longitude)
        # t = s/v
        time = f"{(distance / speed) / 60:.1f}"
        arrival_time.append({
            "station_id" : i.station.id,
            "time" : time
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

    # Convert back to list
    result = list(station_dict.values())
    return result

def update_bus_locations():
    """ update bus current station every 10 minute """
    global BUS_LOCATIONS
    global BUS_ARRIVAL_TIME

    while True:
        buses = fetch_bus_data()

        for bus in buses:
            bus_id = bus.get("bus_id")
            lat = bus.get("latitude")
            lon = bus.get("longitude")
            line = str(bus.get("line"))
            speed = bus.get("speed")

            if bus_id is None or lat is None or lon is None or line not in line_routes:
                continue
            #initailize start station
            if bus_id not in BUS_LOCATIONS:
                start_station = find_nearest_station_line(lat, lon, line_routes[line].objects.all())
                cur_order = line_routes[line].objects.get(station=start_station).order
                current_station = start_station.id
                BUS_LOCATIONS[bus_id] = {
                    "latitude": lat,
                    "longitude": lon,
                    "station_id": current_station,
                    "line": line
                }
            else:
                cur_order = BUS_LOCATIONS[bus_id]["station_id"]

            # find current station
            order = find_current_station(lat, lon, line, cur_order)
            current_station = line_routes[line].objects.get(order=order).station.id
            BUS_LOCATIONS[bus_id] = {
                "latitude": lat,
                "longitude": lon,
                "station_id": current_station,
                "line": line
            }
            """
            line :
             time : [stationid: , time:}
            """
            t = predict_arrival_time(lat, lon, line, speed)
            BUS_ARRIVAL_TIME[bus_id] = {
                "line": line,
                "time": overall_arrival_time(line)
            }

        time.sleep(FETCH_INTERVAL)

thread = threading.Thread(target=update_bus_locations, daemon=True)
thread.start()