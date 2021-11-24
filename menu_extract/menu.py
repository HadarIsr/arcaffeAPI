import requests
import json

ARCAFFE_API = "https://www.10bis.co.il/NextApi/GetRestaurantMenu?culture=en&uiCulture=en&" \
              "restaurantId=19156&deliveryMethod=pickup"

JSON_MENU_PATCH = "daily_menu.json"


def dish_halper(dish) -> dict:
    return {
        "dishId": dish['dishId'],
        "dishName": dish['dishName'],
        "dishPrice": dish['dishPrice'],
        "dishDescription": dish['dishDescription']
    }


def retrieve_dishes(dish_category:str):
    menu = load_menu()
    categories = menu["Data"]["categoriesList"]
    for category in categories:
        if category["categoryName"] == dish_category:
            dishes = category['dishList']
            break

    if dishes:
        return [dish_halper(dish) for dish in dishes]

    raise Exception("Not Found")


def retrieve_dish(dish_id, dish_category):
    dishes = retrieve_dishes(dish_category)
    for dish in dishes:
        if dish["dishId"] == int(dish_id):
            return dish
    raise Exception("Not Found")


def make_order(order: dict):
    price = 0
    for category in order.keys():
        if category:
            for dish_id in order[category]:
                dish = retrieve_dish(dish_id, category.capitalize())
                price += dish['dishPrice']

    return price


def save_menu():
    daily_menu = open('daily_menu.json', 'w')
    response = requests.get(ARCAFFE_API)
    request_body = response.json()
    json.dump(request_body, daily_menu, ensure_ascii=False)


def load_menu():
    daily_menu = open(JSON_MENU_PATCH)
    json_menu = json.load(daily_menu)
    return json_menu





