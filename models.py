from sqlalchemy import Column, Integer, String

# from .database import Base #grabs base class made in database.py
import database 

class PatientData(database.Base):
    __tablename__ = "bed_raw_3054_only"
    
    es_id = Column(Integer, primary_key=True, index=True)
    tstamp_base = Column(String, index=True)
    ts_offset_seconds = Column(String) #should be float
    data = Column(String, index=True)

  
database.Base.metadata.create_all(bind=database.engine)