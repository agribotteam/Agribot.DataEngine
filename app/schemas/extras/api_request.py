from typing import List
from pydantic import BaseModel, Field


class APIRequest(BaseModel):
     pre_requisites: dict = Field(default={})

     class Config:
          validate_assignment = True
          arbitrary_types_allowed = True
