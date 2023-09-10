from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from .associations import book_author_association, book_category_association
from .base import Base

Base = declarative_base()

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String)

    authors = relationship(
        'Author',
        secondary='book_author_association',
        back_populates='books'
    )

    categories = relationship(
        'Category',
        secondary='book_category_association',
        back_populates='books'
    )
