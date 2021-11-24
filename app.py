from fastapi import FastAPI
from routes.menu import router as menu_router
from routes.update_menu import router as update_menu


from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to arrcaffe api."}


app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.include_router(menu_router, tags=["Arrcafe"], prefix="")
app.include_router(update_menu, tags=["Update Menu"], prefix="/admin")

