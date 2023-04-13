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

# def read_item_by_id(item_id: int, db: Session = Depends(get_db)):
#     db_item = crud.get_item_by_id(db, item_id=item_id)
#     if db_item is None:
#         raise HTTPException(status_code=404, detail="Item ID not found")
#     return db_item

# @app.post("/users/", response_model=schemas.User)
# def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
#     db_user = crud.get_user_by_email(db, email=user.email)
#     if db_user:
#         raise HTTPException(status_code=400, detail="Email already registered")
#     return crud.create_user(db=db, user=user)


# @app.get("/users/", response_model=List[schemas.User])
# def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     users = crud.get_users(db, skip=skip, limit=limit)
#     return users


# @app.get("/users/{user_id}", response_model=schemas.User)
# def read_user(user_id: int, db: Session = Depends(get_db)):
#     db_user = crud.get_user(db, user_id=user_id)
#     if db_user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return db_user


# @app.post("/users/{user_id}/items/", response_model=schemas.Item)
# def create_item_for_user(
#     user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
# ):
#     return crud.create_user_item(db=db, item=item, user_id=user_id)


# @app.get("/items/", response_model=List[schemas.Item])
# def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     items = crud.get_items(db, skip=skip, limit=limit)
#     return items

# @app.get("/items/{item_id}", response_model=schemas.Item)
# def read_item_by_id(item_id: int, db: Session = Depends(get_db)):
#     db_item = crud.get_item_by_id(db, item_id=item_id)
#     if db_item is None:
#         raise HTTPException(status_code=404, detail="Item ID not found")
#     return db_item

