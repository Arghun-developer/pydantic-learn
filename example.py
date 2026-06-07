from pydantic import BaseModel;

class User(BaseModel):
    name: str
    age: int
    email: str

# create a user
user = User(name="arghun", age="31", email="arghun.developer@gmail.com")

print(user)