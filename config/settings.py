import os
from dotenv import load_dotenv

load_dotenv()

MQTT_BROKER = os.getenv('MQTT_BROKER_URL')
MQTT_PORT = int(os.getenv('MQTT_BROKER_PORT'))
MQTT_TOPIC = os.getenv('SENSOR_TOPIC')
MQTT_USERNAME = os.getenv('MQTT_USERNAME')
MQTT_PASSWORD = os.getenv('MQTT_PASSWORD')

SENSOR_CONFIGS = [
    {"sensorId": 1, "dataType": "temperatura", "min": 18, "max": 30, "location": "sala"},
    {"sensorId": 2, "dataType": "humedad", "min": 30, "max": 70, "location": "sala"},
    {"sensorId": 3, "dataType": "sonido", "min": 1, "max": 3, "location": "sala"},
    {"sensorId": 4, "dataType": "movimiento", "min": 0, "max": 1, "location": "sala"},
    {"sensorId": 5, "dataType": "fuego", "min": 0, "max": 1, "location": "sala"}
] 