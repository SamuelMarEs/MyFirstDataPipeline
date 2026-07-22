import pandas as pd
from sqlalchemy import create_engine
import re 

def clean_column_name(name : str) -> str:
    # Lowercase, replace spaces/special chars with underscores
    name = name.lower()
    name = re.sub(r'[^a-z0-9_]', '_', name)
    name = re.sub(r'_+', '_', name)  # collapse multiple underscores
    name = name.strip('_')
    return name

# Load the csv data into Pandas DataFrames
weather_csv : pd.DataFrame = pd.read_csv('Data/NYC_Weather_2016_2022.csv')
taxi_duration_csv : pd.DataFrame = pd.read_csv('Data/NYC.csv')

# Clean columns names
weather_csv.columns = [clean_column_name(c) for c in weather_csv.columns]
taxi_duration_csv.columns = [clean_column_name(c) for c in taxi_duration_csv.columns]
# Clean format
weather_csv['time'] = weather_csv['time'].str.replace('T', ' ')

print('CSV files loaded succesfully')

# Create data base
engine = create_engine('sqlite:///nyc_taxi_data.db')
print('Data base created')

# Load DataFrames into SQLite tables
weather_csv.to_sql('weather', con=engine, if_exists='replace', index=False)
taxi_duration_csv.to_sql('taxi_trips', con=engine, if_exists='replace', index=False)
print('DataFrames loaded to data base')

# SQL Query to JOIN the tables
query : str = """
SELECT 
    taxi_trips.id,
    taxi_trips.vendor_id,
    taxi_trips.pickup_datetime,
    taxi_trips.dropoff_datetime,
    taxi_trips.passenger_count,
    taxi_trips.pickup_longitude,
    taxi_trips.pickup_latitude,
    taxi_trips.dropoff_longitude,
    taxi_trips.dropoff_latitude,
    taxi_trips.store_and_fwd_flag,
    taxi_trips.trip_duration,
    weather.temperature_2m_c,
    weather.precipitation_mm,
    weather.rain_mm,
    weather.cloudcover,
    weather.cloudcover_low,
    weather.cloudcover_mid,
    weather.cloudcover_high,
    weather.windspeed_10m_km_h,
    weather.winddirection_10m
FROM 
    taxi_trips
JOIN 
    weather 
    ON SUBSTR(taxi_trips.pickup_datetime, 1, 13) || ':00' = weather.time
"""

# Export the results as a .csv file
result = pd.read_sql_query(query, con=engine)
result.to_csv('taxi_trips.csv', index=False)
# Confirms if the JOIN worked
print(f"Taxi rows: {len(taxi_duration_csv)}")
print(f"Result rows: {len(result)}")
