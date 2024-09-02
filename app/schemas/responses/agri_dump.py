from typing import List, Optional
from pydantic import BaseModel, HttpUrl, Field



    
class GenerateJdResponse(BaseModel):
    response:str = Field(..., example="Successfully Trigered.")