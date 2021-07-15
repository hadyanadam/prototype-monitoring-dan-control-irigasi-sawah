from fastapi import APIRouter, Depends
from fastapi import status
from fastapi.templating import Jinja2Templates
from .controllers import Controllers as Ctrl
from .schemas import SensorData


router = APIRouter()

templates = Jinja2Templates("templates")


def save_data(data: dict):
    with open("app/data.csv", "w") as file:
        file.write(f"{data['flow1']},{data['flow2']},{data['level1']},{data['level2']}")


def get_data() -> list:
    with open("app/data.csv", "r") as file:
        data = file.read().split(",")

    data = {"flow1": data[0], "flow2": data[1], "level1": data[2], "level2": data[3]}
    return data


@router.get("/")
async def index(context: dict = Depends(Ctrl.index)):
    return templates.TemplateResponse(name="index.html", context=context)


@router.post(
    "/api/sensor", response_model=SensorData, status_code=status.HTTP_201_CREATED
)
async def create_sensor_data(sensor: SensorData):
    data = save_data(sensor.dict())
    return data


@router.get("/api/sensor", response_model=SensorData)
async def get_sensor_data():
    data = get_data()
    return data
