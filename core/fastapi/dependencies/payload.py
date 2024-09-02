from fastapi import Header, Request
from app.constants.payload import DEFAULT_PAYLOAD
from app.schemas.extras.api_request import APIRequest
from core.utils import decrypt_and_decompress_instance_payload

async def validate_payload(
     request: Request,
     x_instance_payload_key: str = Header(None, convert_underscores=True),
     x_instance_payload: str = Header(None, convert_underscores=True),
):
     request.apirequest = APIRequest()
     if x_instance_payload and x_instance_payload_key:
          request.apirequest.pre_requisites = decrypt_and_decompress_instance_payload(
               x_instance_payload_key,
               x_instance_payload
          )
     else:
          request.apirequest.pre_requisites = DEFAULT_PAYLOAD