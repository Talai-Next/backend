# service.py
from .external_api_service import fetch_bus_data
from geopy.distance import geodesic
from .buses_location_predictions_service import get_predictions

def feedback_modifier(data):
    lat = data.get("latitude")
    lon = data.get("longitude")

    # this is what it should call
    # buses = get_predictions

    # this is for mockup
    buses = fetch_bus_data()

    closest_bus = None
    min_distance = float("inf")

    for bus in buses:
        distance = geodesic((lat, lon), (bus["latitude"], bus["longitude"])).meters
        if distance < min_distance:
            min_distance = distance
            closest_bus = bus

    if closest_bus:
        data["bus_id"] = int(closest_bus["bus_id"])
        data["bus_line"] = closest_bus["line"]

    # remove lat/lon before saving
    data.pop("latitude", None)
    data.pop("longitude", None)

    return data
