import os
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine(os.getenv('FLASK_DB_URI'))
Base = declarative_base()


class Type(Base):
    __tablename__ = 'types'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
