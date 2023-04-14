from sqlalchemy.orm import Session #we want session so we can declare the type of db parameters
from models import PatientData

def get_patient_by_esid(db: Session, es_id: int):
    print("Hey!")
    print(db.query(PatientData).filter(PatientData.es_id == es_id))
    print("Aye")
    print(db.query(PatientData))
    print("Crey!")
    return db.query(PatientData).filter(PatientData.es_id == es_id).first()
