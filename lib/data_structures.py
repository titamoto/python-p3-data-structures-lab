spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return [value["name"] for value in spicy_foods]

def get_spiciest_foods(spicy_foods):
    spiciest_foods = []
    return [food for food in spicy_foods if food.get("heat_level") > 5]

def print_spicy_foods(spicy_foods):
    [print(f'{food.get("name")} ({food.get("cuisine")}) | Heat Level: ' + '🌶' * food.get("heat_level")) for food in spicy_foods]

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    return [food for food in spicy_foods if food.get("cuisine") == cuisine][0]

def print_spiciest_foods(spicy_foods):
    [print(f'{food.get("name")} ({food.get("cuisine")}) | Heat Level: ' + '🌶' * food.get("heat_level")) for food in spicy_foods if food.get("heat_level") > 5]

def get_average_heat_level(spicy_foods):
    return sum([food.get("heat_level") for food in spicy_foods]) / len(spicy_foods)

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
