from fastapi import APIRouter
from fastapi.logger import logger

router = APIRouter()
@router.get("/v1/agri_dump")
async def agri_dump():
    try:
        logger.info("succuessfully recived the request.")
        return {"Success."}
    except Exception as e:
        return str(e)