import requests

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