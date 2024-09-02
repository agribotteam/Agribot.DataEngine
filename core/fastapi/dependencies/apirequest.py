from fastapi import Request

from app.schemas.extras.api_request import APIRequest


async def get_apirequest(
     request: Request
) -> APIRequest:
     return request.apirequest
