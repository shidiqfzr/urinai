import json
from urllib.request import urlopen
import folium
from streamlit_folium import folium_static
import streamlit as st
import googlemaps
import pandas as pd
from streamlit_js_eval import get_geolocation

def find_hospitals_nearby():
    # Fetch location data using ipinfo.io

    # url = 'https://ipinfo.io/json'
    # response = urlopen(url)
    # data = json.load(response)

    # location = data['loc'].split(',')
    # user_latitude = float(location[0])
    # user_longitude = float(location[1])

    # Fetch location data using get_geolocation
    location = get_geolocation()

    user_latitude = location['coords']['latitude']
    user_longitude = location['coords']['longitude']

    gmaps_api_key = st.secrets["GMAPS_API_KEY"]

    # Initialize the Google Maps client with your API key
    gmaps = googlemaps.Client(key=gmaps_api_key)

    # Search for hospitals near your specified location
    places = gmaps.places_nearby(
        location=(user_latitude, user_longitude),
        keyword='hospital',
        radius=5000  # You can adjust the radius as needed
    )

    # Create a Folium map centered on your specified location
    m = folium.Map(location=[user_latitude, user_longitude], zoom_start=15)

    # Create a list to store hospital details
    hospital_data = []

    # Define a custom icon for the user's location
    user_icon = folium.Icon(color='red', prefix='fa', icon='person')

    # Add a marker for the user's location with the custom icon
    folium.Marker(
        [user_latitude, user_longitude],  
        icon=user_icon,
        tooltip='Your Location'
    ).add_to(m)

    # Add markers for nearby hospitals
    for place in places['results']:
        name = place['name']
        place_lat = place['geometry']['location']['lat']
        place_lng = place['geometry']['location']['lng']

        # Calculate the distance between the user and the hospital
        user_location = (user_latitude, user_longitude)
        hospital_location = (place_lat, place_lng)

        # Use the Google Maps API to find the distance and duration
        distance_matrix = gmaps.distance_matrix(user_location, hospital_location, mode="driving")  # You can adjust the mode

        if distance_matrix['status'] == 'OK':
            distance = distance_matrix['rows'][0]['elements'][0]['distance']['text']
            duration = distance_matrix['rows'][0]['elements'][0]['duration']['text']
        else:
            distance = 'N/A'
            duration = 'N/A'

        # Retrieve details about the hospital
        place_details = gmaps.place(place['place_id'], fields=['name', 'formatted_address', 'rating', 'user_ratings_total', 'formatted_phone_number'])

        if place_details['status'] == 'OK':
            details = place_details['result']
            name = details.get('name', 'No Name')
            address = details.get('formatted_address', 'No Address')
            rating = details.get('rating', None)
            user_ratings_total = details.get('user_ratings_total', None)
            phone_number = details.get('formatted_phone_number', 'No Phone Number')

            # Append hospital details to the list
            hospital_data.append([name, address, phone_number, distance, duration])

            # Create a pop-up HTML for the marker
            html = f'<b>{name}</b><ul style="width: 120px;"><li>Rating: {rating}</li><li>Distance: {distance}</li><li>Duration: {duration}</li></ul>'

            folium.Marker([place_lat, place_lng], tooltip=name, popup=folium.Popup(html)).add_to(m)

    # Create a Pandas DataFrame from the hospital data
    hospital_df = pd.DataFrame(hospital_data, columns=['Nama', 'Alamat', 'Kontak', 'Jarak', 'Waktu Tempuh'])
    
    hospital_df.index = hospital_df.index + 1

    # Display the map with hospital markers in Streamlit
    st.markdown("<h1 style='text-align: center; margin-bottom: 1em;'>Lokasi Rumah Sakit Terdekat</h1>", unsafe_allow_html=True)
    folium_static(m, width=700, height=500)

    # Display the table with hospital details
    st.subheader('Detail Rumah Sakit')
    st.dataframe(hospital_df)

# Example of calling the function
# if __name__ == '__main__':
#     find_hospitals_nearby()