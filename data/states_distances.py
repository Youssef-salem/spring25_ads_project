import pandas as pd
from geopy.distance import geodesic

# Load CSV with states' data
# Data taken from Wikipedia (Updated geographic centers of U.S. states)
statesDF = pd.read_csv('states.csv')

# Create distances DataFrame
distancesDF = pd.DataFrame(columns=["state1", "state2", "distance_km"])

# Compute geodesic distances in kilometers
for state1, lat1, lon1 in zip(statesDF.state, statesDF.latitude, statesDF.longitude):
    for state2, lat2, lon2 in zip(statesDF.state, statesDF.latitude, statesDF.longitude):
        distance_km = geodesic((lat1, lon1), (lat2, lon2)).kilometers
        distancesDF = distancesDF._append({
            "state1": state1,
            "state2": state2,
            "distance_km": round(distance_km, 2)  # Rounded for readability
        }, ignore_index=True)

# Save to CSV
distancesDF.to_csv('state_distances.csv', index=False)
