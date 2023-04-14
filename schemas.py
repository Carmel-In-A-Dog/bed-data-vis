
from pydantic import BaseModel
from datetime import datetime

class Patient(BaseModel):
    es_id: int
    tstamp_base : datetime
    ts_offset_seconds : str
    data : str
    
    class Config:
        orm_mode = True


# class PatientData(PatientDataBase):
#     pass