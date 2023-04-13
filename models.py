from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

# from .database import Base #grabs base class made in database.py
import database 
class PatientData(database.Base):
    __tablename__ = "bed_raw_3054_only"
    
    es_id = Column(Integer, primary_key=True, index=True)
    tstamp_base = Column(String, index=True)
    ts_offset_seconds = Column(String) #should be float
    data = Column(String, index=True)
    
    


#this class is a model b/c it interacts with the db
# class User(Base):
#     __tablename__ = "users"
    
#     id = Column(Integer, primary_key=True, index=True)
#     email = Column(String, unique=True, index=True)
#     hashed_password = Column(String)
#     is_active = Column(Boolean, default=True)
    
#     # contains values from other tables related to this one
#     items = relationship("Item", back_populates="owner")
    
# class Item(Base):
#     __tablename__ = "items"
    
#     id = Column(Integer, primary_key=True, index=True)
#     title = Column(String, index=True)
#     description = Column(String, index=True)
#     owner_id = Column(Integer, ForeignKey("users.id"))
    
#     owner = relationship("User", back_populates="items")
    
    