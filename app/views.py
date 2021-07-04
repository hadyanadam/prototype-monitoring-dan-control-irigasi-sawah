from fastapi import APIRouter, Depends
from fastapi import status
from fastapi.templating import Jinja2Templates
from .controllers import Controllers as Ctrl
from .schemas import SensorData


router = APIRouter()

templates = Jinja2Templates("templates")

data = {
    "flow": 0,
    "level": 0
}

@router.get("/")
async def index(context: dict = Depends(Ctrl.index)):
    return templates.TemplateResponse(name="index.html", context=context)


@router.post('/api/sensor', response_model=SensorData, status_code=status.HTTP_201_CREATED)
async def create_sensor_data(sensor: SensorData):
    data.update({'flow': sensor.flow, 'level': sensor.level})
    return data


@router.get('/api/sensor', response_model=SensorData)
async def get_sensor_data():
    return data