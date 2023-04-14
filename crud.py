from sqlalchemy.orm import Session #we want session so we can declare the type of db parameters
import models, schemas

def get_patient_by_esid(db: Session, es_id: int):
    print("Hey!")
    print(db.query(models.PatientData).filter(models.PatientData.es_id == es_id))
    print("Aye")
    print(db.query(models.PatientData))
    print("Crey!")
    return db.query(models.PatientData).filter(models.PatientData.es_id == es_id).first()
