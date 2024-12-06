import threading
import time
import json
from datetime import datetime
from queue import Queue
from concurrent.futures import ThreadPoolExecutor
from typing import List
from config.settings import MQTT_TOPIC
from models.sensor import SensorConfig, SensorData
from utils.data_generator import generate_sensor_value
import random

class SensorManager:
    def __init__(self, max_workers=10):
        self.sensor_queue = Queue()
        self.executor = ThreadPoolExecutor(max_workers=max_workers)
        self.running = True

    def start_sensor(self, sensor_config: SensorConfig):
        def sensor_task():
            while self.running:
                sensor_data = generate_sensor_value(sensor_config)
                self.sensor_queue.put(sensor_data)
                time.sleep(random.uniform(1, 3))

        self.executor.submit(sensor_task)

    def start_publisher(self, mqtt_client):
        def publish_task():
            while self.running:
                sensors = []
                try:
                    # Usar un timeout para no bloquear indefinidamente
                    while not self.sensor_queue.empty():
                        sensors.append(self.sensor_queue.get(timeout=0.1))
                    
                    if sensors:
                        message = {
                            "userId": 1,
                            "timestamp": datetime.now().isoformat(),
                            "sensors": [vars(sensor) for sensor in sensors]
                        }
                        # Publicar de manera asíncrona
                        self.executor.submit(
                            mqtt_client.client.publish,
                            MQTT_TOPIC,
                            json.dumps(message)
                        )
                except Exception as e:
                    print(f"Error en publicación: {e}")
                
                time.sleep(5)

        self.executor.submit(publish_task)

    def shutdown(self):
        self.running = False
        self.executor.shutdown(wait=True) 