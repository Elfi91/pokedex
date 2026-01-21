# 📱 Django Pokédex Project

[![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-5.x-green?style=flat-square&logo=django)](https://www.djangoproject.com/)

> [!IMPORTANT]
> 🚧 **Work In Progress** 🚧
> This project is currently under active development.

## 📖 About
This project is a functional Pokédex application designed to showcase a full-stack integration using **Django**. It manages a relational database of Pokémon specimens, providing both a clean **Web UI** for users and a set of **REST-like APIs** for developers to interact with the data.

## 🚀 Key Features

- **Dynamic Web Interface**: A responsive card-based layout with type-based color coding (e.g., Yellow for Electric, Red for Fire).
- **Advanced Pokémon Model**: Tracks Pokedex IDs, Primary/Secondary Types, Abilities, Levels, Genders (with custom icons), and optional Nicknames.
- **Automatic Sorting**: The Pokédex is automatically sorted by the official Pokedex ID.
- **Full CRUD API**: Support for Listing, Adding, Updating, and Deleting Pokémon via JSON requests.
- **Partial Updates**: Intelligent update logic that only modifies provided fields while keeping others intact.

## 🛠️ Tech Stack
- **Backend**: Python, Django.
- **Frontend**: HTML5, CSS3 (Flexbox & Grid).
- **Database**: SQLite (inspected via DBeaver).
- **API Testing**: Postman.

## 📸 Web Interface Preview
The interface features custom cards with:
- **Gender Icons**: ♂ for Male, ♀ for Female, and ? for Unknown.
- **Type Badges**: Color-coded labels for each Pokémon type.
- **Dynamic Borders**: The top border of each card reflects the Pokémon's primary type color.

## ⚙️ Installation & Setup

1.  Clone the repository:
    ```bash
    git clone [https://github.com/Elfi91/pokedex.git](https://github.com/Elfi91/pokedex.git)
    cd pokedex
    ```

2.  Setup Virtual Environment:
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

5.  Run Server::
    ```bash
    python manage.py runserver
    ```
    Visit the UI at: http://127.0.0.1:8000/pokemon/web-list/

## 🛠️ Recommended Tools

### Postman (API Testing)
To test the API endpoints:
1. Open **Postman** and create a new collection named "Pokedex".
2. Add new requests for each endpoint listed in the table above.
3. For `POST` requests, remember to set the **Body** to `raw` and select `JSON` as the format.

### DBeaver (Database Management)
To inspect or manually edit the SQLite database:
1. Open **DBeaver** and create a new connection.
2. Select **SQLite** as the database type.
3. Browse to the `db.sqlite3` file located in the project root directory.
4. Open the `pokemon_pokemon` table to view, edit, or delete records directly.

## 📡 API Endpoints

Use a tool like **Postman** to interact with the following endpoints. All POST requests require a JSON body.

| Method | Endpoint | Description | Status Code |
| :--- | :--- | :--- | :--- |
| **GET** | `/pokemon/list/` | Retrieves the full list of Pokémon in JSON format, sorted by Pokedex ID. | `200 OK` |
| **POST** | `/pokemon/add/` | Adds a new Pokémon to the database. Fields: `name`, `pokedex_id`, `type_1`, `level`, etc. | `201 Created` |
| **POST** | `/pokemon/update/<id>/` | Partially updates an existing Pokémon using its UUID. | `200 OK` |
| **GET** | `/pokemon/delete/<id>/` | Removes a specific Pokémon from the collection. | `200 OK` |

### Example JSON Body for `add` or `update`:
```json
{
    "name": "Pikachu",
    "pokedex_id": 25,
    "level": 15,
    "type_1": "Electric",
    "ability": "Static",
    "gender": "M",
    "nickname": "Sparky"
}
```
