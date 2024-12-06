from config.settings import SENSOR_CONFIGS
from core.mqtt_client import MQTTClient
from core.sensor_manager import SensorManager
from models.sensor import SensorConfig
import time
import signal

def main():
    mqtt_client = MQTTClient()
    mqtt_client.connect()

    # Crear gestor de sensores con un pool de 10 hilos
    sensor_manager = SensorManager(max_workers=10)

    # Manejar señales de terminación
    def signal_handler(signum, frame):
        print("\nFinalizando aplicación...")
        sensor_manager.shutdown()
        mqtt_client.disconnect()
        exit(0)

    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    # Iniciar sensores
    for config in SENSOR_CONFIGS:
        sensor_config = SensorConfig(**config)
        sensor_manager.start_sensor(sensor_config)

    # Iniciar publicador
    sensor_manager.start_publisher(mqtt_client)

    # Mantener la aplicación en ejecución
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        signal_handler(signal.SIGINT, None)

if __name__ == "__main__":
    main() 