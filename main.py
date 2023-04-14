from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud, models, schemas, database
# from .database import SessionLocal, engine

models.database.Base.metadata.create_all(bind=database.engine)

app = FastAPI()


# Dependency
def get_db(): # gets called to start the communcication with db
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


# @app.get("/sensor/Tables/bed_data_3054_only/{es_id}", response_model=schemas.PatientDataBase)
@app.get("/Schemas/sensor/Tables/bed_data_3054_only/{es_id}", response_model=schemas.PatientDataBase)
def read_patient_by_esid(es_id: int, db: Session = Depends(get_db)):
    db_patient = crud.get_patient_by_esid(db, es_id=es_id)
    if db_patient is None:
        raise HTTPException(status_code=404, detail="es_id not found")
    return db_patient
