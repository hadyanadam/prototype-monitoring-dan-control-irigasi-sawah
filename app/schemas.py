from pydantic import BaseModel


class SensorData(BaseModel):
    flow1: float
    level1: float
    flow2: float
    level2: float


class RelayData(BaseModel):
    val: bool


class RelayAllData(BaseModel):
    relay1: int
    relay2: int