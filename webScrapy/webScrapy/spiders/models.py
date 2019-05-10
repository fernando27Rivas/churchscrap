from sqlalchemy import create_engine, Column, Table, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    Integer, SmallInteger, String, Date, DateTime, Float, Boolean, Text, LargeBinary)

from scrapy.utils.project import get_project_settings

DeclarativeBase = declarative_base()

def db_connect():
    """
    Performs database connection using database settings from settings.py.
    Returns sqlalchemy engine instance
    """
    return create_engine(get_project_settings().get("CONNECTION_STRING"))

def create_table(engine):
    DeclarativeBase.metadata.create_all(engine)

class QuoteDB(DeclarativeBase):
    __tablename__ = "conference2"

    id = Column(Integer, primary_key=True)
    year = Column('year', String(50))
    speaker = Column('speaker', Text())
    topic = Column('topic', Text())
    url = Column('url', Text())
    headline = Column('headline', Text())
    words = Column('words', Text())