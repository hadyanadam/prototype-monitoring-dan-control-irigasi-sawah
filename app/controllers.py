from fastapi import Request


class Controllers:
    def __init__():
        pass

    def index(request: Request):
        context = {
            "request": request,
            "list_sawah": [
                {
                    "id": 1,
                    "name": "Sawah 1",
                },
                {
                    "id": 2,
                    "name": "Sawah 2",
                }
            ]
        }
        return context
