from sqlalchemy.orm import Session #we want session so we can declare the type of db parameters
import models, schemas

def get_patient_by_esid(db: Session, es_id: int):
    print("Hey!")
    print(db.query(models.PatientData).filter(models.PatientData.es_id == es_id))
    print("Aye")
    print(db.query(models.PatientData))
    print("Crey!")
    return db.query(models.PatientData).filter(models.PatientData.es_id == es_id).first()


# SELECT x.*
# from bed_raw_3054_only x
# fetch first 50 rows only

# def get_user(db: Session, user_id: int):
#     return db.query(models.User).filter(models.User.id == user_id).first()

# def get_user_by_email(db: Session, email: str):
#     return db.query(models.User).filter(models.User.email == email).first()

# def get_users(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.User).offset(skip).limit(limit).all()


# def create_user(db: Session, user: schemas.UserCreate):
#     fake_hashed_password = user.password + "notreallyhashed"
#     db_user = models.User(email=user.email, fake_hashed_password=fake_hashed_password) # create instance
#     db.add(db_user) #add instance to object
#     db.commit() #commit changes to db
#     db.refresh(db_user) # refresh instance
#     return db_user

# def get_items(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.Item).offset(skip).limit(limit).all()

# def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
#     db_item = models.Item(**item.dict(), owner_id=user_id)
#     db.add(db_item)
#     db.commit()
#     db.refresh(db_item)
#     return db_item

# def get_item_by_id(db: Session, item_id: int):
#     return db.query(models.Item).filter(models.Item.id == item_id).first()