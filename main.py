from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import dal
from schemas import Patient
from models import PatientData
# from .database import SessionLocal, engine

app = FastAPI()

# Dependency
def get_db(): # gets called to start the communcication with db
    # I'd probably move this to the database file ~eddyizm~
    db = dal.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/patient_bed_data/{es_id}", response_model=Patient)
def read_patient_by_esid(es_id: int, db: Session = Depends(get_db)):
    response = db.query(PatientData).filter(PatientData.es_id == es_id).first()
    if not response:
         raise HTTPException(status_code=404, detail="Item not found")
    return response
