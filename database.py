from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.author import Base as AuthorBase
from models.category import Base as CategoryBase
from models.books import Base as BookBase

DATABASE_URL = 'sqlite:///library.db'
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

AuthorBase.metadata.create_all(engine)
CategoryBase.metadata.create_all(engine)
BookBase.metadata.create_all(engine)

def init_db():
    AuthorBase.metadata.create_all(bind=engine)
    CategoryBase.metadata.create_all(bind=engine)
    BookBase.metadata.create_all(bind=engine)
