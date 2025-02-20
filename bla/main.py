import uvicorn
from injector import Injector

from bla.infrastructure.api import create_api

api = create_api(Injector())

if __name__ == "__main__":
    uvicorn.run("main:api")
