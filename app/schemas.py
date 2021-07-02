from pydantic import BaseModel


class SensorData(BaseModel):
    flow: float
    level: float
