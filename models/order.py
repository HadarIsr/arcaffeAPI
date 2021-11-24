from pydantic import BaseModel, Field

class OrderModer(BaseModel):
    drinks: list = Field(default=None)
    desserts: list = Field(default=None)
    pizzas: list = Field(default=None)

    class Config:
        schema_extra = {
            "example": {
                "drinks": '[id_5, id_6]',
                "desserts": '[id_1, id_2]',
                "pizzas": '[id_3, id_4]'
        }
    }