import pytest
from click.testing import CliRunner
from main import cli
from database import init_db, SessionLocal
from models.author import Author
from models.category import Category

runner = CliRunner()

@pytest.fixture
def database():
    # Set up the test database using SQLite in-memory
    engine = create_engine('sqlite:///:memory:')
    SessionLocal.configure(bind=engine)
    init_db(engine)

    # Create a test author and category for use in the test
    session = SessionLocal()
    author = Author(name="Test Author")
    category = Category(name="Test Category")
    session.add_all([author, category])
    session.commit()
    session.close()

    yield  # This is where the test function runs

    # Clean up the test database after the test function finishes
    engine.dispose()

def test_add_book(database):
    result = runner.invoke(cli, ['add_book', '--title', 'Test Book', '--author_id', '1', '--category_id', '1'])

    assert result.exit_code == 0
    assert 'Book Test Book added.' in result.output
