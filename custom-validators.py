from pydantic import BaseModel, field_validator

class User(BaseModel):
    name: str
    age: int

    @field_validator("age")
    def age_must_be_positive(cls, value):
        if value < 0:
            raise ValueError("Age must be positive value")
        return value
    
    @field_validator
    def name_must_not_be_empty(cls, value):
        if not value.strip():
            raise ValueError("name can not be empty value")
        return value.strip() # you can also transform value here
    

user = User(name="", age=-4)

print(user)