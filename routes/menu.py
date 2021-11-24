from fastapi import APIRouter, HTTPException, Body
from fastapi.encoders import jsonable_encoder
from menu_extract import menu
from models import order


router = APIRouter()


@router.get("/drinks")
def get_drinks():
    try:
        drinks = menu.retrieve_dishes("Drinks")
        return drinks
    except Exception as ex:
        raise HTTPException(status_code=404, detail=str(ex))


@router.get("/drink/{drink_id}")
def get_drink(drink_id: int):
    try:
        drink = menu.retrieve_dish(drink_id, "Drinks")
        return drink

    except Exception as ex:
        raise HTTPException(status_code=404, detail=str(ex))


@router.get("/pizzas")
def get_pizzas():
    try:
        pizzas = menu.retrieve_dishes("Pizzas")
        return pizzas
    except Exception as ex:
        raise HTTPException(status_code=404, detail=str(ex))


@router.get("/pizza/{pizza_id}")
def get_pizza(pizza_id: str):
    try:
        pizza = menu.retrieve_dish(pizza_id, "Pizza")
        return pizza

    except Exception as ex:
        raise HTTPException(status_code=404, detail=str(ex))


@router.get("/desserts")
def get_desserts():
    try:
        desserts = menu.retrieve_dishes("Desserts")
        return desserts
    except Exception as ex:
        raise HTTPException(status_code=404, detail=str(ex))


@router.get("/dessert/{dessert_id}")
def get_pizza(dessert_id: str):
    try:
        dessert = menu.retrieve_dish(dessert_id, "Desserts")
        return dessert

    except Exception as ex:
        raise HTTPException(status_code=404, detail=str(ex))


@router.post("/order")
def post_order(order: order.OrderModer = Body(...)):
    try:
        order = jsonable_encoder(order)
        order_price = menu.make_order(order)
        return {"price": order_price}

    except Exception as ex:
        raise HTTPException(status_code=404, detail=str(ex))


