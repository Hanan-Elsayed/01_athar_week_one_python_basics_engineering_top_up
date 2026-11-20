import os

import requests
from dotenv import load_dotenv

load_dotenv()
 

class Meal:
    """One meal taken from the API response."""

    def __init__(self, name, category, area, instructions):
        self.name = name
        self.category = category
        self.area = area
        self.instructions = instructions

    def summary(self):
        text = self.instructions.replace("\r\n", " ").replace("\n", " ")
        if len(text) > 220:
            text = text[:220] + "..."
        return (
            f"Meal: {self.name}\n"
            f"Category: {self.category}\n"
            f"Area: {self.area}\n"
            f"How to make it: {text}"
        )


def fetch_meal(api_key, meal_name):
    url = f"https://www.themealdb.com/api/json/v1/{api_key}/search.php"
    response = requests.get(url, params={"s": meal_name}, timeout=15)
    response.raise_for_status()
    return response.json()


def main():
    api_key = os.getenv("MEALDB_API_KEY")
    if not api_key:
        raise SystemExit("Missing MEALDB_API_KEY. Add it to the .env file.")

    data = fetch_meal(api_key, "Arrabiata")
    meals = data.get("meals")
    if not meals:
        raise SystemExit("The API returned no meals.")

    first = meals[0]
    meal = Meal(
        name=first["strMeal"],
        category=first["strCategory"],
        area=first["strArea"],
        instructions=first["strInstructions"],
    )
    print(meal.summary())


if __name__ == "__main__":
    main()
