from sqlalchemy import create_engine
from models import Base

DATABASE_URL = 'sqlite:///library.db'  # Replace with your database URL
engine = create_engine(DATABASE_URL)

Base.metadata.create_all(engine)
