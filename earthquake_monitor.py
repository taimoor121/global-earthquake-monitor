import requests
from datetime import datetime, timedelta

# --------------------------------------------------
# GLOBAL EARTHQUAKE MONITOR
# --------------------------------------------------

# Use UTC date
today = datetime.utcnow().date()
tomorrow = today + timedelta(days=1)

url = "https://earthquake.usgs.gov/fdsnws/event/1/query"

params = {
    "format": "geojson",
    "starttime": today.isoformat(),
    "endtime": tomorrow.isoformat()
}

# --------------------------------------------------
# Download earthquake data
# --------------------------------------------------

try:
    response = requests.get(
        url,
        params=params,
        timeout=30
    )

    response.raise_for_status()

except requests.exceptions.ConnectionError:
    print("\nERROR: Could not connect to USGS.")
    print("Please check your internet connection.")
    exit()

except requests.exceptions.Timeout:
    print("\nERROR: USGS request timed out.")
    print("Please try again later.")
    exit()

except requests.exceptions.HTTPError as error:
    print("\nERROR: USGS returned an HTTP error.")
    print(f"Details: {error}")
    exit()

try:
    data = response.json()

except ValueError:
    print("\nERROR: USGS returned an invalid response.")
    print("The service may be temporarily unavailable.")
    exit()

# --------------------------------------------------
# Get earthquake list
# --------------------------------------------------

earthquakes = data.get("features", [])

if not earthquakes:
    print("\nNo earthquakes were found for today.")
    exit()

# --------------------------------------------------
# Remove events with missing magnitude
# --------------------------------------------------

valid_earthquakes = [
    earthquake
    for earthquake in earthquakes
    if earthquake["properties"].get("mag") is not None
]

if not valid_earthquakes:
    print("\nEarthquakes were downloaded, but no valid magnitudes were found.")
    exit()

# --------------------------------------------------
# Find largest earthquake
# --------------------------------------------------

largest = max(
    valid_earthquakes,
    key=lambda earthquake: earthquake["properties"]["mag"]
)

properties = largest["properties"]
coordinates = largest["geometry"]["coordinates"]

magnitude = properties["mag"]
location = properties.get("place", "Unknown")
event_id = largest["id"]

latitude = coordinates[1]
longitude = coordinates[0]
depth = coordinates[2]

event_time = datetime.utcfromtimestamp(
    properties["time"] / 1000
)

event_url = (
    f"https://earthquake.usgs.gov/"
    f"earthquakes/eventpage/{event_id}"
)

# --------------------------------------------------
# Display result
# --------------------------------------------------

print("=" * 55)
print("             GLOBAL EARTHQUAKE MONITOR")
print("=" * 55)

print(f"\nDate (UTC): {today.strftime('%d %B %Y')}")
print(f"Earthquakes detected: {len(earthquakes)}")

print("\nLARGEST EARTHQUAKE")
print("-" * 55)

print(f"Magnitude  : {magnitude}")
print(f"Location   : {location}")
print(f"Depth      : {depth:.1f} km")
print(f"Latitude   : {latitude:.4f}")
print(f"Longitude  : {longitude:.4f}")
print(f"Time (UTC) : {event_time.strftime('%Y-%m-%d %H:%M:%S')}")

print(f"\nUSGS Event:")
print(event_url)

print("\n" + "=" * 55)
