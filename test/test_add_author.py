import pytest
from click.testing import CliRunner
from sqlalchemy import create_engine
from main import cli
from database import init_db, SessionLocal
from models.author import Author

runner = CliRunner()

@pytest.fixture
def database():
    # Set up the test database using SQLite in-memory
    engine = create_engine('sqlite:///:memory:')
    SessionLocal.configure(bind=engine)
    init_db(engine)

    # Create a test author for use in the test
    session = SessionLocal()
    author = Author(name="Test Author")
    session.add(author)
    session.commit()
    session.close()

    yield  
    engine.dispose()

def test_add_author(database):
    result = runner.invoke(cli, ['add_author', '--name', 'Test Author'], input='Test Author\n')

    assert result.exit_code == 0
    assert 'Author Test Author added.' in result.output
