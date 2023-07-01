```python
import geopy
from geopy.geocoders import Nominatim

database_connection = None  # This should be replaced with actual database connection

def get_location_by_coordinates(lat, lon):
    geolocator = Nominatim(user_agent="social_media_app")
    location = geolocator.reverse([lat, lon])
    return location.address

def get_coordinates_by_location(location):
    geolocator = Nominatim(user_agent="social_media_app")
    location = geolocator.geocode(location)
    return (location.latitude, location.longitude)

def save_user_location(user_id, lat, lon):
    location = get_location_by_coordinates(lat, lon)
    query = "UPDATE UserSchema SET location = %s WHERE id = %s"
    cursor = database_connection.cursor()
    cursor.execute(query, (location, user_id))
    database_connection.commit()

def get_user_location(user_id):
    query = "SELECT location FROM UserSchema WHERE id = %s"
    cursor = database_connection.cursor()
    cursor.execute(query, (user_id,))
    result = cursor.fetchone()
    return result[0] if result else None
```