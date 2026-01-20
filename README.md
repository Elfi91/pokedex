# Pokedex

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

2.  Open your browser or use a tool like Postman/curl to interact with the API:
    -   `GET /pokemon/list/`: Get the list of Pokemon.
    -   `GET /pokemon/add/`: Add a new Pokemon.
    -   `GET /pokemon/delete/<uuid>/`: Delete a Pokemon by its UUID.
