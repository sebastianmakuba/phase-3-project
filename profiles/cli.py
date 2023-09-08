import click
from database import init_db, SessionLocal
from models import Author, Category, Book

@click.group()
def cli():
    pass

@click.command()
@click.option('--name', prompt='Author Name', help='Name of the author')
def add_author(name):
    session = SessionLocal()
    author = Author(name=name)
    session.add(author)
    session.commit()
    session.close()
    click.echo(f'Author {name} added.')

@click.command()
@click.option('--name', prompt='Category Name', help='Name of the category')
def add_category(name):
    session = SessionLocal()
    category = Category(name=name)
    session.add(category)
    session.commit()
    session.close()
    click.echo(f'Category {name} added.')

@click.command()
@click.option('--title', prompt='Book Title', help='Title of the book')
@click.option('--author_id', prompt='Author ID', type=int, help='Author ID')
@click.option('--category_id', prompt='Category ID', type=int, help='Category ID')
def add_book(title, author_id, category_id):
    session = SessionLocal()
    book = Book(title=title, author_id=author_id, category_id=category_id)
    session.add(book)
    session.commit()
    session.close()
    click.echo(f'Book {title} added.')

# @click.command()
# def list_books():
#     session = SessionLocal()
#     books = session.query(Book).all()
#     session.close()
#     if books:
#         for book in books:
#             click.echo(f'{book.id}: {book.title} by {book.author.name} ({book.category.name})')
#     else:
#         click.echo('No books found.')
@click.command()
def list_books():
    session = SessionLocal()
    books = session.query(Book).all()

    for book in books:
        # Load the author and category attributes before closing the session
        author_name = book.author.name
        category_name = book.category.name

        click.echo(f'{book.id}: {book.title} by {author_name} ({category_name})')

    session.close()

@click.command()
@click.option('--book-id', prompt='Book ID', help='ID of the book to update')
@click.option('--new-title', prompt='New Title', help='New title for the book') 
def update_book(book_id, new_title):
    session = SessionLocal()
    book = session.query(Book).filter(Book.id == book_id).first()

    if book:
        book.title = new_title
        session.commit()
        session.close()
        click.echo(f'Book {book_id} updated.')
    else:
        click.echo(f'Book with ID {book_id} not found.')

@click.command()
@click.option('--book-id', prompt='Book ID', help='ID of the book to delete')
def delete_book(book_id):
    session = SessionLocal()
    book = session.query(Book).filter(Book.id == book_id).first()

    if book:
        session.delete(book)
        session.commit()
        session.close()
        click.echo(f'Book {book_id} deleted.')
    else:
        click.echo(f'Book with ID {book_id} not found.')
cli.add_command(add_author)
cli.add_command(add_category)
cli.add_command(add_book)
cli.add_command(update_book)
cli.add_command(delete_book)
cli.add_command(list_books)
