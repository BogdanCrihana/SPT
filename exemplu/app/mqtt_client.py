import paho.mqtt.client as mqtt
from app.sensor_data_generator import generate_sensor_data

# MQTT Broker details
BROKER_URL = "90e53740d0f446b8aef77a5fab1303ac.s2.eu.hivemq.cloud"
BROKER_PORT = 8883

CERTIFICATE_FILE = "C:\\Users\\Bobo\\Desktop\\isrgrootx1.pem"

# MQTT Credentials
USERNAME = "BogdanCrihana"
PASSWORD = "Unitbv2024"

# Topics for sensor data
TEMPERATURE_TOPIC = "house/temperature"
HUMIDITY_TOPIC = "house/humidity"
PRESSURE_TOPIC = "house/pressure"

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker")
        # Subscribe to topics
        client.subscribe([(TEMPERATURE_TOPIC, 0), (HUMIDITY_TOPIC, 0), (PRESSURE_TOPIC, 0)])
    else:
        print(f"Connection to MQTT Broker failed with code: {rc}")

def on_message(client, userdata, message):
    topic = message.topic
    payload = message.payload.decode()
    print(f"Received data from {topic}: {payload}")

def get_sensor_data():
    # Fetch fresh sensor data each time this function is called
    return generate_sensor_data()

# Initialize MQTT client
client = mqtt.Client()
client.username_pw_set(USERNAME, PASSWORD)
client.tls_set(CERTIFICATE_FILE)

# Set up callback functions
client.on_connect = on_connect
client.on_message = on_message

# Connect to MQTT broker
client.connect(BROKER_URL, BROKER_PORT)

# Start the MQTT client loop
client.loop_start()
