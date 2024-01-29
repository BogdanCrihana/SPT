# app/sensor_data_generator.py

import random

def generate_sensor_data():
    """
    Generates random sensor data for temperature, humidity, and pressure
    """
    temperature = round(random.uniform(18.0, 25.0), 2)  # Temperature in Celsius
    humidity = round(random.uniform(40.0, 60.0), 2)     # Humidity in percentage
    pressure = round(random.uniform(980.0, 1020.0), 2)  # Pressure in hPa

    return {
        "temperature": temperature,
        "humidity": humidity,
        "pressure": pressure
    }
