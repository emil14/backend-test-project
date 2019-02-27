import os
from sqlalchemy import create_engine, Column, ARRAY, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine(os.getenv('FLASK_DB_URI'))
Session = sessionmaker(bind=engine)
Base = declarative_base()


class Type(Base):
    __tablename__ = 'types'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    props_ids = Column(ARRAY(Integer))


class Prop(Base):
    __tablename__ = 'props'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))


class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    type_id = Column(Integer)
