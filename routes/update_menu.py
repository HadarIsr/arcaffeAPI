from fastapi import APIRouter, HTTPException
from menu_extract import menu

USER_NAME = "admin"
PASSWORD = "admin"

router = APIRouter()


@router.get("/update_menu/{admin}/{password}")
def get_new_menu(admin: str, password: str):
    if admin == USER_NAME and password == PASSWORD:
        menu.save_menu()
    else:
        raise HTTPException(status_code=405, detail="Wrong username or password")
