from fastapi import APIRouter, Depends
from fastapi import status
from fastapi.templating import Jinja2Templates
from .controllers import Controllers as Ctrl
from .schemas import RelayData, SensorData

router = APIRouter()

templates = Jinja2Templates("templates")


def save_data(data: dict):
    with open("app/data.csv", "w") as file:
        file.write(f"{data['flow1']},{data['flow2']},{data['level1']},{data['level2']}")


def save_relay_data(id: int, val: bool):
    with open(f"app/relay{id}.txt", "w") as file:
        file.write(f"{int(val)}")


def get_data() -> dict:
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
    return sensor.dict()


@router.get("/api/sensor", response_model=SensorData)
async def get_sensor_data():
    data = get_data()
    return data


@router.get("/api/relay/{id}", response_model=RelayData)
async def get_relay_data(id: int):
    file = open(f"app/relay{id}.txt", "r")
    data = file.read()
    file.close()
    return {"val": data}


@router.post("/api/relay/{id}", response_model=RelayData)
async def update_relay_data(id: int, relay: RelayData):
    data = save_relay_data(id, relay.val)
    return relay.dict()
