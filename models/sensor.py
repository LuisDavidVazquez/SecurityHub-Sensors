from dataclasses import dataclass
from typing import Union, Literal

@dataclass
class SensorData:
    sensorId: int
    dataType: str
    data: Union[float, bool]
    location: str

@dataclass
class SensorConfig:
    sensorId: int
    dataType: Literal["temperatura", "humedad", "sonido", "movimiento", "fuego"]
    min: float
    max: float
    location: str 