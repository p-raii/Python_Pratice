from geopy.geocoders import Nominatim

def get_coordinates(place_name):
    # Initialize the geolocator
    geolocator = Nominatim(user_agent="my_geocoder")

    try:
        # Use geolocator to get location information
        location = geolocator.geocode(place_name)

        if location:
            latitude = location.latitude
            longitude = location.longitude
            print(f"Place: {place_name}")
            print(f"Latitude: {latitude}")
            print(f"Longitude: {longitude}")
        else:
            print(f"Location information not found for {place_name}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    place_name = "kathmandu"
    get_coordinates(place_name)
