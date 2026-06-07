from pydantic import BaseModel;

class User(BaseModel):
    name: str
    age: int
    email: str

# create a user
user = User(name="arghun", age="3asdsd1", email="arghun.developer@gmail.com")

print(user)