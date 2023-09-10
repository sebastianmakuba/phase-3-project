from sqlalchemy import Column, Integer, String
from .base import Base



class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    name = Column(String)

