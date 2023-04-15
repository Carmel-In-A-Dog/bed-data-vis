from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# DB_USER="no_snooping!"
# DB_PASSWORD="no_snooping!"
# DB_SERVER="no_snooping!"
# DB_PORT=5432
# DB_NAME="no_snooping!"

# SQLALCHEMY_DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_SERVER}:{DB_PORT}/{DB_NAME}"

SQLALCHEMY_DATABASE_URL = 'sqlite:///test.db'
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo = True, connect_args={'check_same_thread': False})

connection = engine.connect()

# session establishes converstion with db
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# base class stores a catlog of classes and mappsed tables
Base = declarative_base() 