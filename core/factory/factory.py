from app.schemas.extras.api_request import APIRequest
from core.fastapi.dependencies.apirequest import get_apirequest
from app.source import agriController

from fastapi import Depends

class Factory:
    """
    This is the factory container that will instantiate all the controllers and
    repositories which can be accessed by the rest of the application.
    """

    def get_job_description_controller(self, api_request: APIRequest = Depends(get_apirequest)):
        return agriController(api_request=api_request)
