from ..models import StationLocation, LineOneRoute, LineThreeRoute, LineFiveRoute, LineSpecialRoute
import requests
from .search_service import find_nearest_station_line, find_distance
import time
import threading

FETCH_INTERVAL = 10
BUS_LOCATIONS = {}

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

def find_current_station(lat,lon,line,order):
    """
    Check if the bus has entered the 300m radius of the next station and update the order.
    """

    next_station = line_routes[line].objects.get(order=order+1).station
    # if last station
    if not next_station:
        # update order to first station
        return 1
    distance = find_distance(lat,lon,next_station.latitude,next_station.longitude)
    if distance <= 300:
        order = order + 1
    return order



def update_bus_locations():
    """ update bus current station every 10 minute """
    global BUS_LOCATIONS

    while True:
        buses = fetch_bus_data()

        for bus in buses:
            bus_id = bus.get("bus_id")
            lat = bus.get("latitude")
            lon = bus.get("longitude")
            line = str(bus.get("line"))
            cur_order = 0

            if bus_id is None or lat is None or lon is None or line not in line_routes:
                print("eieie")
                continue
            print("yaya")
            #initailize start station
            if bus_id not in BUS_LOCATIONS:
                start_station = find_nearest_station_line(lat, lon, line_routes[line].objects.all())
                cur_order = line_routes[line].objects.get(station=start_station).order
                current_station = start_station.id
                BUS_LOCATIONS[bus_id] = {
                    "latitude": lat,
                    "longitude": lon,
                    "station_id": current_station
                }
            else:
                cur_order = BUS_LOCATIONS[bus_id]["station_id"]

            # find current station
            order = find_current_station(lat, lon, line, cur_order)
            current_station = line_routes[line].objects.get(order=order).station.id
            BUS_LOCATIONS[bus_id] = {
                "latitude": lat,
                "longitude": lon,
                "station_id": current_station
            }

        time.sleep(FETCH_INTERVAL)

thread = threading.Thread(target=update_bus_locations, daemon=True)
thread.start()