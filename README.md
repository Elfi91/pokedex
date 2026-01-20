# Pokedex

> [!IMPORTANT]
> 🚧 **Work In Progress** 🚧
> This project is currently under active development.

A simple Django application to manage a Pokedex.

## Features

- **List Pokemon**: View a list of all your Pokemon.
- **Add Pokemon**: Add new Pokemon to your collection (currently hardcoded to Bulbasaur for testing).
- **Delete Pokemon**: Release a Pokemon into the wild.
- **English Interface**: All API responses and comments are in English.

## Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/Elfi91/pokedex.git
    cd pokedex
    ```

2.  Create and activate a virtual environment:
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3.  Install dependencies:
    ```bash
    pip install django
    ```

4.  Apply migrations:
    ```bash
    python manage.py migrate
    ```

## Usage

1.  Start the development server:
    ```bash
    python manage.py runserver
    ```

2.  Open your browser or use a tool like **Postman** or **curl** to interact with the API:
    -   `GET /pokemon/list/`: Get the list of Pokemon.
    -   `GET /pokemon/add/`: Add a new Pokemon.
    -   `GET /pokemon/delete/<uuid>/`: Delete a Pokemon by its UUID.

## Recommended Tools

### Postman
Use Postman to test the API endpoints. You can create a new collection for "Pokedex" and add requests for the endpoints listed above.

### DBeaver
Use DBeaver to inspect the SQLite database:
1.  Open DBeaver.
2.  Create a new connection and select **SQLite**.
3.  Browse to the `db.sqlite3` file in the project directory.
4.  You can now view and edit the `pokemon_pokemon` table directly.
