from pydantic import BaseModel, StrictStr
from typing import Optional

class AgriDumpRequest(BaseModel):

    query: StrictStr
       
