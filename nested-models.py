from pydantic import BaseModel
from typing import Optional

class Address(BaseModel):
    street: str
    city: str
    country: Optional[str] = None

class User(BaseModel):
    name: str
    age: int
    address: Address

user = User(
    name="arghun",
    age=30,
    address={
        "street": "test",
        "city": "istanbul",
    }
)

print(user)