from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    name = Column(String)

class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String)

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    author_id = Column(Integer, ForeignKey('authors.id'))
    category_id = Column(Integer, ForeignKey('categories.id'))
    author = relationship('Author', back_populates='books')
    category = relationship('Category', back_populates='books')

Author.books = relationship('Book', back_populates='author')
Category.books = relationship('Book', back_populates='category')
