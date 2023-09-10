from sqlalchemy import ForeignKey, Column, Integer, Table
from sqlalchemy.orm import relationship
from .base import Base
from .author import Author
from .category import Category



# Define association tables
book_author_association = Table(
    'book_author_association',
    Base.metadata,
    Column('book_id', Integer, ForeignKey('books.id')),
    Column('author_id', Integer, ForeignKey('authors.id'))
)

book_category_association = Table(
    'book_category_association',
    Base.metadata,
    Column('book_id', Integer, ForeignKey('books.id')),
    Column('category_id', Integer, ForeignKey('categories.id'))
)

# Define the relationships between Author, Category, and Book
books = relationship(
    'Book',
    secondary=book_author_association,
    back_populates='authors'
)
books = relationship(
    'Book',
    secondary=book_category_association,
    back_populates='categories'
)
