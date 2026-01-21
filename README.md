# Pokedex

> [!IMPORTANT]
> 🚧 **Work In Progress** 🚧
> This project is currently under active development.


A simple Django application to manage a Pokedex.

## Features

- **Web Interface**: View your Pokemon collection in a user-friendly web page.
- **List Pokemon**: Retrieve a list of all your Pokemon via API.
- **Add Pokemon**: Add new Pokemon to your collection using JSON data.
- **Update Pokemon**: Update existing Pokemon details.
- **Delete Pokemon**: Release a Pokemon into the wild.

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

2.  **Web Interface**:
    -   Open your browser and visit: `http://127.0.0.1:8000/pokemon/web-list/`

3.  **API Endpoints**:
    Use a tool like **Postman** or **curl** to interact with the API:
    -   `GET /pokemon/list/`: Get the list of all Pokemon.
    -   `POST /pokemon/add/`: Add a new Pokemon. Requires a JSON body with fields like `name`, `pokedex_id`, `type_1`, etc.
    -   `POST /pokemon/update/<uuid>/`: Update a Pokemon's details. Requires a JSON body.
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
