import random
from models.sensor import SensorData, SensorConfig

def generate_sensor_value(sensor_config: SensorConfig) -> SensorData:
    if sensor_config.dataType in ["temperatura", "humedad", "sonido"]:
        data = round(random.uniform(sensor_config.min, sensor_config.max), 2)
    else:
        data = random.choice([True, False])
        
    return SensorData(
        sensorId=sensor_config.sensorId,
        dataType=sensor_config.dataType,
        data=data,
        location=sensor_config.location
    ) 