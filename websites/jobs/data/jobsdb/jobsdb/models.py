import datetime
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import URL
from jobsdb.settings import DATABASE, TABLE_NAME

DeclarativeBase = declarative_base()

def db_connect():
    return create_engine(URL.create(**DATABASE))

def create_jobsdb_table(engine):
    DeclarativeBase.metadata.create_all(engine)

class Jobsdb(DeclarativeBase):
    __tablename__ =  TABLE_NAME

    id = Column(Integer, primary_key=True)
    title = Column('title', String(500))
    link = Column('link', Text())
    time = Column('time', String(500))
    created_date = Column(DateTime, default=datetime.datetime.now())
