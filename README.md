# Week 01 — Python Basics & Engineering Top-Up

## Assignment

Build a short Python program that calls a public REST API, reads the JSON it sends back, stores that data in a small class, and prints a formatted summary.

The program must run inside a virtual environment, and the API key must be read from a `.env` file. The key must not be written in the Python code.

The week covers five ideas:

- Object-Oriented programming in Python
- Virtual environments (`venv`)
- HTTP and REST
- JSON
- keeping secrets out of source code

## Requirements

| Requirement                 | How this project meets it                                           |
| --------------------------- | ------------------------------------------------------------------- |
| Virtual environment         | Dependencies are installed in `.venv`, not into the system Python.  |
| API key from a file         | `MEALDB_API_KEY` lives in `.env`. `main.py` loads it at startup.    |
| Call a public REST API      | `requests.get` sends an HTTP GET to TheMealDB search endpoint.      |
| Parse JSON                  | `response.json()` turns the response text into a Python dictionary. |
| Store the result in a class | `Meal` keeps the name, category, area, and cooking instructions.    |
| Print a formatted summary   | `meal.summary()` prints a short readable block.                     |

## What the program does

`main.py` searches TheMealDB for "Arrabiata". The API answers with JSON. The program takes the first meal, stores it in a `Meal` object, and prints a summary like this:

```text
Meal: Spicy Arrabiata Penne
Category: Vegetarian
Area: Italian
How to make it: Bring a large pot of water to a boil...
```

TheMealDB publishes a public test key, `1`. That value sits in `.env`, and the program reads it from there.

## How the solution is put together

```text
.env          the API key (not committed)
.gitignore    keeps .env and .venv out of git
.venv/        the virtual environment
main.py       the program
```

The run follows six steps:

1. `load_dotenv()` reads `.env` and puts `MEALDB_API_KEY` into the environment.
2. `main` reads that key with `os.getenv`. If the key is missing, the program stops with a clear message.
3. `fetch_meal` sends a GET request to `https://www.themealdb.com/api/json/v1/1/search.php` with the meal name as a query parameter. The key is the `1` in that path.
4. `raise_for_status()` stops the program if the API returns an error code.
5. `response.json()` parses the JSON. `Meal` copies `strMeal`, `strCategory`, `strArea`, and `strInstructions` onto a new object.
6. `summary` shortens a long instruction text and prints the name, category, area, and steps.

`requests` performs the HTTP call. `python-dotenv` reads the `.env` file. Both are installed only inside `.venv`.

## How to run it

From this folder:

```bash
source .venv/bin/activate
python main.py
```

`.env` should contain one line:

```bash
MEALDB_API_KEY=1
```

`1` is TheMealDB's public test key. Leave `.env` untracked. `.gitignore` already lists it.
