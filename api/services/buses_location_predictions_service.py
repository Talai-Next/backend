import threading
import time
from geopy.distance import geodesic
from queue import Queue
from  .external_api_service import fetch_bus_data

BUS_PREDICTIONS = {}  # Dictionary to store predictions per bus
FETCH_INTERVAL = 10  # Fetch new data every 10 seconds
TIME_STEP = 1  # Serve one location per second
NUM_PREDICTIONS = 10  # Number of future predictions per bus
MOVEMENT_FACTOR = 1 / 3600  # Convert speed (km/h) to movement per second


def generate_predictions(bus):
    """Generate 10 future locations based on speed using geopy. (this should be AI)"""
    predictions = []
    current_lat = bus.get("latitude", 13.000000)  # Default to fixed starting position
    current_lon = bus.get("longitude", 100.000000)
    speed = bus.get("speed", 0)  # Speed in km/h
    direction = 90  # Assume movement east

    obj_id = bus.get("id", None) # object ID
    bus_id = bus.get("bus_id", None) # real bus ID
    line = bus.get("line", 1)

    if bus_id is None:
        print("Error: Bus data missing 'id'. Skipping entry.")
        return []

    for _ in range(NUM_PREDICTIONS):
        if speed > 0:
            distance_km = speed * MOVEMENT_FACTOR * TIME_STEP  # Calculate movement
            new_location = geodesic(kilometers=distance_km).destination(
                (current_lat, current_lon), direction
            )
            current_lat, current_lon = new_location.latitude, new_location.longitude

        predictions.append({
            "id": obj_id,
            "bus_id": bus_id,
            "line": line,
            "latitude": round(current_lat, 6),
            "longitude": round(current_lon, 6),
            "speed": speed,
        })

    return predictions

def update_bus_data():
    """Fetches data every 10 seconds and pre-generates 10 locations per bus."""
    global BUS_PREDICTIONS
    while True:
        raw_data = fetch_bus_data()

        # Update predictions for each bus
        for bus in raw_data:
            bus_id = bus.get("id")
            if bus_id is None:
                continue

            new_predictions = generate_predictions(bus)

            # If bus ID doesn't exist in dictionary, create a new queue
            if bus_id not in BUS_PREDICTIONS:
                BUS_PREDICTIONS[bus_id] = Queue()

            # Clear old predictions and add new ones
            while not BUS_PREDICTIONS[bus_id].empty():
                BUS_PREDICTIONS[bus_id].get()

            for prediction in new_predictions:
                BUS_PREDICTIONS[bus_id].put(prediction)

        time.sleep(FETCH_INTERVAL)

def get_predictions():
    return BUS_PREDICTIONS

# Start the background thread
def start_update_bus_data():
    thread = threading.Thread(target=update_bus_data, daemon=True)
    thread.start()