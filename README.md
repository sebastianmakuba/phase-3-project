# Library Management CLI

This is a command-line interface (CLI) application for managing a library with books, authors, and categories. It allows you to add and list books, authors, and categories using a SQLite database and SQLAlchemy Object-Relational Mapping (ORM).

## Features

- Add new authors to the database.
- Add new categories to the database.
- Add new books to the database, associating them with authors and categories.
- List all books in the library, including their titles, authors, and categories.

## Prerequisites

- Python 3.10+
- Pipenv (for managing virtual environments)

## Installation

1. Clone this repository to your local machine:

   ```shell
   git clone git@github.com:sebastianmakuba/phase-3-project.git
   ```

2. Navigate to the project directory:

   ```shell
   cd phase-3-project
   ```

3. Install the required dependencies using Pipenv:

   ```shell
   pipenv install
   ```

4. Initialize the database:

   ```shell
   pipenv run python -c "from database import init_db; init_db()"
   ```

## Usage

To run the CLI application, use the following command:

```shell
pipenv run python main.py
```

### Commands

- `add_author`: Add a new author to the database.
- `add_category`: Add a new category to the database.
- `add_book`: Add a new book to the database, associating it with an author and a category.
- `list_books`: List all books in the library.

### Examples

#### Add an Author

```shell
pipenv run python main.py add_author --name "J.K. Rowling"
```

#### Add a Category

```shell
pipenv run python main.py add_category --name "Fantasy"
```

#### Add a Book

```shell
pipenv run python main.py add_book --title "Harry Potter and the Philosopher's Stone" --author_id 1 --category_id 1
```

#### List Books

```shell
pipenv run python main.py list_books
```

