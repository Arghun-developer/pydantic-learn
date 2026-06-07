from pydantic import BaseModel
from typing import List

class Order(BaseModel):
    item: str
    quantity: int

class User(BaseModel):
    customer_number: int
    orders: List[Order]

user = User(
    customer_number=343,
    orders=[{ "item": "test1", "quantity": 30 }, { "item": "test2", "quantity": 54 }]
)

print(user)