from pydantic import BaseModel, EmailStr, validator, field_validator

from dataclasses import dataclass

# type validating using dataclasses (before pydantic)
@dataclass
class Person:
    name: str
    age: int
    
    
# using pydantic
class User(BaseModel):
    name: str
    email: EmailStr # to use EmailStr, install pydantic[email] extension
    account_id: int
    
    @validator("account_id") # deprecated (Pydantic V1 style), just for demonstration
    def validate_account_id(cls, value):
        if value <= 0:
            raise ValueError(f"account_id must be a positive integer: {value}")
        return value
    
    
class Person(BaseModel):
    name: str
    account_id: int
    
    @field_validator("account_id") # (Pydantic V2 style) OK
    def validate_account_id(cls, value):
        if value <= 0:
            raise ValueError(f"account_id must be a positive integer: {value}")
        return value
    

# two different ways of creating an object using pydantic model

# using keyword arguments
user1 = User(
    name="John",
    email="john@place.com",
    account_id=1123
)

# using unpacking
user_data = {
    'name': "Jack",
    'account_id': 1124
}

user2 = Person(**user_data)

# Pydantic provides JSON serialization

user2.json() # deprecated (Pydantic V1 style)

user2.model_dump_json() # Pydantic V2 style OK

# we can also get a dict
user2.dict() # deprecated
user2.model_dump()

# to convert json string back to pydantic model:
json_str = '{"name": "Bob", "account_id": 1125}'
person1 = Person.parse_raw(json_str) # deprecated
person1 = Person.model_validate_json(json_str)