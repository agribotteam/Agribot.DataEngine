from fastapi import FastAPI
import logging

from shared.logger import setup_logging
setup_logging()
logger = logging.getLogger('AGRI_DUMP')

app = FastAPI()

@app.get("/v1/agri_dump")
async def agri_dump():
    try:
        
        return {"Success."}
    except Exception as e:
        return str(e)
