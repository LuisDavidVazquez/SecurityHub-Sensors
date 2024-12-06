import paho.mqtt.client as mqtt
from config.settings import MQTT_BROKER, MQTT_PORT, MQTT_USERNAME, MQTT_PASSWORD

class MQTTClient:
    def __init__(self):
        self.client = mqtt.Client()
        self.client.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)
        self.client.on_connect = self._on_connect
        self.client.on_message = self._on_message

    def _on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print("Conectado exitosamente al broker MQTT")
        else:
            print(f"Error al conectar con el broker MQTT, código de error: {rc}")

    def _on_message(self, client, userdata, msg):
        print(f"Mensaje recibido en el tópico {msg.topic}: {msg.payload.decode()}")

    def connect(self):
        self.client.connect(MQTT_BROKER, MQTT_PORT, 60)
        self.client.loop_start()

    def disconnect(self):
        self.client.loop_stop()
        self.client.disconnect() 