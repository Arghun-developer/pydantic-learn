from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    name: str
    age: int
    email: str
    is_adming: bool = False # always false is the default
    bio: Optional[str] = None # optional, defaults is None

arghunUser = {
    "name": "arghun",
    "age": 31,
    "email": "arghun.developer@gmail.com"
}

user = User(**arghunUser)

print(user)
