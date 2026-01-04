from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, declarative_base


SQLALCHEMY_DB_URL = 'sqlite:///./blog.db'

eng = create_engine(SQLALCHEMY_DB_URL,connect_args={"check_same_thread":False})

SessionLocal = sessionmaker(bind=eng,autocommit=False,autoflush=False)

Base = declarative_base()