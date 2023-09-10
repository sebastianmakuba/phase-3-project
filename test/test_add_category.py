import pytest
from click.testing import CliRunner
from main import cli
from database import init_db, SessionLocal
from models.category import Category

runner = CliRunner()

@pytest.fixture
def database():
    # Set up the test database using SQLite in-memory
    engine = create_engine('sqlite:///:memory:')
    SessionLocal.configure(bind=engine)
    init_db(engine)

    # Create a test category for use in the test
    session = SessionLocal()
    category = Category(name="Test Category")
    session.add(category)
    session.commit()
    session.close()

    yield  # This is where the test function runs

    # Clean up the test database after the test function finishes
    engine.dispose()

def test_add_category(database):
    result = runner.invoke(cli, ['add_category', '--name', 'Test Category'], input='Test Category\n')

    assert result.exit_code == 0
    assert 'Category Test Category added.' in result.output
