from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from .associations import book_author_association, book_category_association
from .base import Base



class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String)

    authors = relationship(
        'Author',
        secondary='book_author_association',
        backref= 'books'
    )

    categories = relationship(
        'Category',
        secondary='book_category_association',
        backref ='books'
    )
