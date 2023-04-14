# MODELS IN THIS FILE ARE PYDANTIC MODELS(SCHEMEAS). DIFFERENT FROM SQLALCHEMY

from pydantic import BaseModel
from typing import Union, List
from datetime import datetime

class PatientDataBase(BaseModel):
    id: int
    tstamp_base = datetime
    ts_offset_seconds = str
    data = str
    
    class Config:
        orm_mode = True

class PatientData(PatientDataBase):
    pass
