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

# class ItemBase(BaseModel):
#     title: str
#     description: Union[str, None] = None # might be busted
    
# class ItemCreate(ItemBase):
#     pass

# class Item(ItemBase):
#     id: int
#     owner_id: int
    
#     # use this so we get relationship data with sqlalchemy
#     class Config:
#         orm_mode = True
        
# class UserBase(BaseModel):
#     email: str

# class UserCreate(UserBase):
#     password: str

# class User(UserBase):
#     id: int
#     is_active: bool
#     items: List[Item] = []
    
#     class Config:
#         orm_mode = True
    